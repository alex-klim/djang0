from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Category')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=15)
    birthday = models.DateTimeField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title