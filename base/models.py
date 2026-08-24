from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models


class User(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username


class Mascota(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = 'disponible', 'Disponible'
        EN_PROCESO = 'en_proceso', 'En proceso'
        ADOPTADA = 'adoptada', 'Adoptada'

    class Especie(models.TextChoices):
        PERRO = 'perro', 'Perro'
        GATO = 'gato', 'Gato'
        OTRO = 'otro', 'Otro'

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=Especie.choices)
    raza = models.CharField(max_length=80, blank=True, null=True)
    edad = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.DISPONIBLE,
    )

    publicado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mascotas_publicadas'
    )

    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        APROBADA = 'aprobada', 'Aprobada'
        RECHAZADA = 'rechazada', 'Rechazada'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='solicitudes_realizadas'
    )

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='solicitudes'
    )

    mensaje = models.TextField(blank=True, null=True)

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )

    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.usuario.username} para {self.mascota.nombre}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'mascota'],
                name='unique_solicitud_usuario_mascota',
            )
        ]
