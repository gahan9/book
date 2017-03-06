from django.contrib import admin

from .models import Author, Publisher, book

admin.site.register(Publisher)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pub', 'rating', 'published_date')

admin.site.register(book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'maximum_book', 'minimum_book')

admin.site.register(Author, AuthorAdmin)