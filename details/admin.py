from django.contrib import admin

from .models import Author, Publisher, book

admin.site.register({ book, Publisher, Author})