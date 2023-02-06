from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Author, Book, Biography


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class BookSerializer(ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'
