from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Author, Book, Biography


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer2(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name']


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class BookSerializer(ModelSerializer):
    # authors = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'
