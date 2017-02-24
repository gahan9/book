from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name


class book(models.Model):
	name = models.CharField(max_length=50)
	author = models.ManyToManyField(Author)
	pub = models.ForeignKey(Publisher)
	price = models.FloatField(validators = [MinValueValidator(0.9)])

	def __str__(self):
		return self.name
