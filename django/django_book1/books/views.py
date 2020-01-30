from django.shortcuts import render
from django.views import generic
from django.apps import apps

from .models import Book, Author, Publisher


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['django_app', 'books', 'programmers_test']
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        print('\n\n\n HomeView.get_context_data() context >>>>> ', context)
        return context

class BooksModelView(generic.TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        """
        add context data being drawn in the template.
        """
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

class BookList(generic.ListView):
    model = Book

class AuthorList(generic.ListView):
    model = Author

class PublisherList(generic.ListView):
    model = Publisher

class BookDetail(generic.DetailView):
    model = Book

class AuthorDetail(generic.DetailView):
    model = Author

class PublisherDetail(generic.DetailView):
    model = Publisher