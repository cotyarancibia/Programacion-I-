from rest_framework import status
from rest_framework.test import APITestCase

from base.models import User


class AuthenticationAndPermissionsTests(APITestCase):
    def create_user(self, username, role=User.Role.CLIENTE):
        return User.objects.create_user(
            username=username,
            password='StrongPassword2026!',
            role=role,
        )

    def authenticate_with_jwt(self, user):
        response = self.client.post(
            '/api/token/',
            {'username': user.username, 'password': 'StrongPassword2026!'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
        return response.data

    def test_register_creates_cliente_without_exposing_id(self):
        response = self.client.post(
            '/api/users/register/',
            {
                'username': 'newuser',
                'password': 'StrongPassword2026!',
                'email': 'newuser@example.com',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('id', response.data)
        self.assertEqual(User.objects.get(username='newuser').role, User.Role.CLIENTE)

    def test_register_rejects_weak_password(self):
        response = self.client.post(
            '/api/users/register/',
            {'username': 'newuser', 'password': '123'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_token_obtain_rejects_invalid_credentials(self):
        self.create_user('user')

        response = self.client.post(
            '/api/token/',
            {'username': 'user', 'password': 'incorrect'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_requires_jwt_authentication(self):
        response = self.client.get('/api/users/profile/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_returns_authenticated_user_and_role(self):
        user = self.create_user('client')
        self.authenticate_with_jwt(user)

        response = self.client.get('/api/users/profile/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['role'], User.Role.CLIENTE)

    def test_logout_blacklists_refresh_token(self):
        user = self.create_user('user')
        tokens = self.authenticate_with_jwt(user)

        response = self.client.post(
            '/api/users/logout/',
            {'refresh': tokens['refresh']},
            format='json',
        )
        refresh_response = self.client.post(
            '/api/token/refresh/',
            {'refresh': tokens['refresh']},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_rejects_invalid_refresh_token(self):
        user = self.create_user('user')
        self.authenticate_with_jwt(user)

        response = self.client.post(
            '/api/users/logout/',
            {'refresh': 'not-a-token'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mascotas_requires_authentication(self):
        response = self.client.get('/api/mascotas/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cliente_cannot_create_mascota(self):
        cliente = self.create_user('client')
        self.authenticate_with_jwt(cliente)

        response = self.client.post('/api/mascotas/', self.mascota_data(), format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_vendedor_can_create_mascota(self):
        vendedor = self.create_user('seller', User.Role.VENDEDOR)
        self.authenticate_with_jwt(vendedor)

        response = self.client.post('/api/mascotas/', self.mascota_data(), format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['publicado_por'], vendedor.id)

    def test_admin_can_create_mascota(self):
        admin = self.create_user('admin', User.Role.ADMIN)
        self.authenticate_with_jwt(admin)

        response = self.client.post('/api/mascotas/', self.mascota_data(), format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['publicado_por'], admin.id)

    @staticmethod
    def mascota_data():
        return {
            'nombre': 'Mora',
            'especie': 'perro',
            'edad': 3,
        }
