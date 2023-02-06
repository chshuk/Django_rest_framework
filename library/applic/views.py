from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .models import Author, Biography, Book
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer, AuthorSerializer2
from rest_framework import permissions, generics


class AuthorViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MyAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer = AuthorSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorSerializer
        return AuthorSerializer2
