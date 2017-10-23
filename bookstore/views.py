from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookstore.models import *
from django.template.loader import get_template
from bookstore.forms import BookPostForm
from .tasks import generate_thumbnail


def index(request):
    books = Book.objects.order_by('year')
    template = get_template('bookstore/index.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))

def create_category(request):
    if request.POST:
        category = Category(title=request.POST.get('title', 'blank'))
        category.save()
        HttpResponseRedirect('/index/')
    return HttpResponse(get_template('bookstore/form.html').render({}, request))

def books(request):
    template = get_template('bookstore/books.html')
    books = Book.objects.all().prefetch_related('authors')
    context = {
        'books':books
    }
    return HttpResponse(template.render(context, request))

def book_details(request, pk):
    template = get_template('bookstore/book_detail.html')
    book = Book.objects.get(pk=pk)
    context = {
        'book':book
    }
    return HttpResponse(template.render(context, request))

def add_book(request):
    if request.method =='POST':
        form = BookPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            book = Book.objects.get(title=request.POST['title'])
            generate_thumbnail(book.id)
            return HttpResponse("gege")
        return HttpResponse("Almost baby")
    elif request.method == 'GET':
        template = get_template('bookstore/add_book.html')
        context = {
            'form':BookPostForm()
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse('OOPS')