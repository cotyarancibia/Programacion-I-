from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Mascota, Solicitud


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('id', 'username', 'email', 'telefono')
    search_fields = ('username', 'email')
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Informacion adicional', {'fields': ('telefono', 'direccion')}),
    )


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
