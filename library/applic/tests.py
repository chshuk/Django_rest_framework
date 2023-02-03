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
