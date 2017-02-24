from django.contrib import admin

from .models import Author,Publisher,book

admin.site.register(Author)
admin.site.register(book)
admin.site.register(Publisher)