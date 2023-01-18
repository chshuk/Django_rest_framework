from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from .models import Author, Biography, Book, Article
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer, ArticleSerializer, ArticleAPISerializer



class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAPIView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleAPISerializer(articles, many=True)
        return Response(serializer.data)
