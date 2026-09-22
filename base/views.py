from rest_framework import permissions, viewsets
from .models import User, Mascota, Solicitud
from .serializers import UserSerializer, MascotaSerializer, SolicitudSerializer


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        if isinstance(obj, Mascota):
            return obj.publicado_por == request.user
        if isinstance(obj, Solicitud):
            return obj.usuario == request.user
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    filterset_fields = ['estado', 'especie', 'publicado_por']
    search_fields = ['nombre', 'especie', 'raza']

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]
    filterset_fields = ['estado', 'mascota']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Solicitud.objects.all()
        return Solicitud.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
