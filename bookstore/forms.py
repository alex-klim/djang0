from django.forms import ModelForm

from .models import Book


class BookPostForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'year', 'price', 'image', 'authors', 'category']