from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookstore.models import *
from django.template.loader import get_template


def index(request):
    books = Book.objects.order_by('year')[:5]
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