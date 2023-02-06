from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .models import Author, Biography, Book
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer
from rest_framework import permissions


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


class MyAPIView(ViewSet):

    def list(self, request):
        print(request.version)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return  Response(serializer.data)

    @action(detail=False, methods=['get'])
    def new_data(self, request):
        return Response({'data': 'NEW data'})
