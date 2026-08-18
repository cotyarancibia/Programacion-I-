from rest_framework import serializers

from base.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        password = validated_data.pop('password')

        user = User(
            **validated_data,
            role=User.Role.CLIENTE
        )

        user.set_password(password)
        user.save()

        return user
class ProfileSerializer(serializers.ModelSerializer):
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
            'role',
        ]