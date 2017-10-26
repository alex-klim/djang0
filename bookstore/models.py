import os

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    def get_image_path(instance, filename):
        return os.path.join(str(instance.title), filename)

    def get_thumb_path(instance):
        return os.path.join(str(instance.title), 'thumb')

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to=get_image_path, default='/None/none.jpg')
    thumbnail = ProcessedImageField(upload_to=get_thumb_path, default='/None/none.jpg')
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/books/%i/" % self.pk

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

class Comment(models.Model):
    author = models.CharField(max_length=25, default='cold-hearted machine')
    comment = models.TextField(max_length=300)
    mark = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    book = models.ForeignKey(Book)