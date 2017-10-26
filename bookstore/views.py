from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookstore.models import *
from django.template.loader import get_template
from bookstore.forms import *
from .tasks import generate_thumbnail
from django.views.generic import FormView, TemplateView, UpdateView, DetailView, ListView
from django.db.models import Avg


class AddBookView(FormView):
    template_name = 'bookstore/add_book.html'
    form_class = BookPostForm
    success_url = '/index/'

    def form_valid(self, form):
        form.save()
        return super(AddBookView, self).form_valid(form)

class AddCategoryView(FormView):
    template_name = 'bookstore/add_category.html'
    form_class = CategoryPostForm
    success_url = '/index/'

    def form_valid(self, form):
        form.save()
        return super(AddCategoryView, self).form_valid(form)

class AddAuthorView(FormView):
    template_name = 'bookstore/add_author.html'
    form_class = AuthorPostForm
    success_url = '/index/'

    def form_valid(self, form):
        form.save()
        return super(AddAuthorView, self).form_valid(form)

class AddCommentView(FormView):
    template_name = 'bookstore/add_comment.html'
    form_class = CommentPostForm
    success_url = '/index/'

    # def form_valid(self, form):
    #     form.save()
    #     return super(AddCommentView, self).form_valid(form)

    # def get_context(self, **kwargs):
    #     context = super(AddCommentView, self).get_context_data(**kwargs)
    #     context['id'] = self.kwargs['book.id']
    #     print(context)
    #     return context

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = CommentPostForm(request.POST,
                               request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
            return HttpResponseRedirect('/index/')
        return HttpResponse("Error")

    def get(self, request, pk):
        template = get_template('bookstore/add_comment.html')
        context = {
            'book': Book.objects.get(pk=self.kwargs.get('pk')),
            'form': CommentPostForm()
        }
        return HttpResponse(template.render(context, request))

class IndexView(ListView):
    template_name = 'bookstore/index.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['books'] = Book.objects.all().annotate(rank=Avg('comment__mark')).order_by('-rank')
        return context

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'bookstore/update_book.html'
    form_class = BookPostForm

class DetailsBookView(DetailView):
    template_name = 'bookstore/book_detail.html'
    context_object_name = 'book'
    model = Book

def books(request):
    template = get_template('bookstore/books.html')
    books = Book.objects.all().prefetch_related('authors')
    context = {
        'books':books
    }
    return HttpResponse(template.render(context, request))