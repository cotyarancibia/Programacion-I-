from django.contrib import admin
from .models import User, Mascota, Solicitud


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'telefono')
    search_fields = ('username', 'email')


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especie', 'estado', 'publicado_por')
    list_filter = ('estado', 'especie')
    search_fields = ('nombre', 'especie')


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mascota', 'estado', 'fecha_solicitud')
    list_filter = ('estado',)
    search_fields = ('usuario__username', 'mascota__nombre')