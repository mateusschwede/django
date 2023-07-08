from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100, blank=True)
	author = models.CharField(max_length=100, blank=True)
	isbn = models.CharField(max_length=100, blank=True)
	publisher = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.title