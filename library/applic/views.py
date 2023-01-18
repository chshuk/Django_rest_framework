from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .models import Author, Biography, Book, Article
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer, ArticleSerializer, ArticleAPISerializer, \
    ArticleSetSerializer


class AuthorViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleViewSet(ViewSet):

    @action(detail=True, methods=['get'])
    def article_name_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.name': article.name})

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSetSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleAPIView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleAPISerializer(articles, many=True)
        return Response(serializer.data)


class ArticleListAPIView(ListAPIView):
    # renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleQuerysetFilterViewSet(ModelViewSet):
    serializer_class = ArticleSetSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()

    def get_queryset(self):
        return Article.objects.filter(name__contains='Пушкин')


class ArticleDjangoFilterViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSetSerializer
    filterset_fields = ['name', 'author']


