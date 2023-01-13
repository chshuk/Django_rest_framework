from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude = ['id']


class BookSerializer(HyperlinkedModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'
