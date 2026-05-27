from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, MascotaViewSet, SolicitudViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'solicitudes', SolicitudViewSet)

urlpatterns = [
    path('', include(router.urls)),
]