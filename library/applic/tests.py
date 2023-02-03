from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase, force_authenticate
from django.contrib.auth.models import User
from .views import AuthorViewSet
from .models import Author, Book


# Create your tests here.
class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_list(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/authors/')
    #     view = AuthorViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birth_year': 1799
        })
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birth_year': 1799
        })
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '1111')
        force_authenticate(request, admin)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(first_name='Лев', last_name='Толстой', birth_year=1828)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Лев', last_name='Толстой', birth_year=1828)
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Александр', 'last_name': 'Пушкин', 'birth_year': 1799})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Лев', last_name='Толстой', birth_year=1828)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '1111')
        client.login(username='admin', password='1111')

        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Lev', 'last_name': 'Tolstoy', 'birth_year': 1910})
        author = Author.objects.get(pk=author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Lev')
        self.assertEqual(author.last_name, 'Tolstoy')
        self.assertEqual(author.birth_year, 1910)
        client.logout()


