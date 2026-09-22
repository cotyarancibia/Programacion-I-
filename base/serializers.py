from rest_framework import serializers
from .models import User, Mascota, Solicitud


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'telefono',
            'direccion',
            'password',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = [
            'id',
            'nombre',
            'especie',
            'raza',
            'edad',
            'descripcion',
            'estado',
            'publicado_por',
            'fecha_publicacion',
        ]
        read_only_fields = ['publicado_por', 'fecha_publicacion']


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = [
            'id',
            'usuario',
            'mascota',
            'mensaje',
            'estado',
            'fecha_solicitud',
        ]
        read_only_fields = ['usuario', 'estado', 'fecha_solicitud']
