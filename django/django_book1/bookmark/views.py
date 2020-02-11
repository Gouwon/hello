from django.shortcuts import render
from django.views import generic

from .models import Bookmark


# Create your views here.
class BookmarkListView(generic.ListView):
    model = Bookmark

class BookmarkDetailView(generic.DetailView):
    model = Bookmark