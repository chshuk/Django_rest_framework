from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_year = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(Author, models.PROTECT)
