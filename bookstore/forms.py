from django.forms import ModelForm

from .models import Book, Category, Author, Comment


class BookPostForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'year', 'price', 'image', 'authors', 'category']

class CategoryPostForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class AuthorPostForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthday', 'bio']

class CommentPostForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['book']