from rest_framework import generics, permissions
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'detail': 'Token invalido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            # El access token sigue valido hasta su propia expiracion.
            return Response(
                {"detail": "Sesion cerrada correctamente."},
                status=status.HTTP_200_OK
            )
        except TokenError:
            return Response(
                {"detail": "Token invalido."},
                status=status.HTTP_400_BAD_REQUEST
            )
