from django.contrib import admin

from .models import *

admin.site.register(Publisher)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pub', 'rating', 'published_date')

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'maximum_book', 'minimum_book')

admin.site.register(Author, AuthorAdmin)


class BookRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'book', 'created')

admin.site.register(BookRating, BookRatingAdmin)
