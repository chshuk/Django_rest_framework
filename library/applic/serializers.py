from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Author, Book, Biography


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class BookSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
