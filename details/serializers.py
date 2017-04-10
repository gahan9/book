from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Author, Book, BookRating, Publisher


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'maximum_book')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['url', 'name', 'author', 'price', 'published_date']


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('url', 'name')
