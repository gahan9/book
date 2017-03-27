from __future__ import unicode_literals
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg, Func


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    maximum_book = models.IntegerField(default=0)
    minimum_book = models.IntegerField(default=0)

    def Round(Func):
        function = 'ROUND'
        template = '%(function)s(%(expressions)s, 1)'

    @property
    def author_rating(self):
        book_instance = Book.objects.filter(author=self)
        xy = []
        for b in book_instance:
            book_filtered = BookRating.objects.filter(book=b).aggregate(avg=Round(Avg('rating')))
            if book_filtered['avg'] is not None:
                xy.append(book_filtered['avg'])
        if len(xy) > 0:
            return "%.1f" % (sum(xy)/len(xy))
        else:
            return "0"

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name='Book Name')
    image = models.ImageField(null=True, blank=True, verbose_name='Book Image')
    author = models.ManyToManyField(Author)
    rating = models.DecimalField(null=True, blank=True, verbose_name='Expert Rating', max_digits=2, decimal_places=1)
    pub = models.ForeignKey(Publisher)
    price = models.FloatField(validators=[MinValueValidator(0.9)], verbose_name='Book Price')
    published_date = models.DateField(blank=True, null=True, verbose_name='Date of Book published')
    availability = models.BooleanField(default=False, verbose_name='available for sale or not.')

    def __str__(self):
        return self.name


class BookRating(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    rating = models.IntegerField(null=True, blank=True, default=None)
    book = models.ForeignKey(Book, related_name='book_rating')
    created = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return 'Profile of user: {}'.format(self.user.username)

    def __str__(self):
        return self.rating
