from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    author = models.CharField(max_length=16, verbose_name='作者')