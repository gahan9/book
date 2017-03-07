from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='user')
#     phone = models.CharField(max_length=20, blank=True, default='')
#     city = models.CharField(max_length=100, default='', blank=True)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    maximum_book = models.IntegerField(default=0)
    minimum_book = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    author = models.ManyToManyField(Author)
    rating = models.FloatField(null=True, blank=True)
    pub = models.ForeignKey(Publisher)
    price = models.FloatField(validators=[MinValueValidator(0.9)])
    published_date = models.DateField(null=True)

    def __str__(self):
        return self.name
