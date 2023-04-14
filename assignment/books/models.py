from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class BooksDetails(models.Model):
    title = models.CharField(max_length=300,blank=True, null=True)
    author = models.CharField(max_length=200,blank=True, null=True)
    authors = models.CharField(max_length=300,blank=True, null=True)
    isbn13 = models.BigIntegerField(blank=True, null=True)
    isbn10 = models.CharField(max_length=100,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    publisher = models.CharField(max_length=150,blank=True, null=True)
    pubyear = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=300,blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    dimensions = models.CharField(max_length=300,blank=True, null=True)

   