from django.shortcuts import render
from django.views import generic

from .models import Album, Photo


# Create your views here.
class AlbumListView(generic.ListView):
    model = Album

class AlbumDetailView(generic.DetailView):
    model = Album

class PhotoDetailView(generic.DetailView):
    model = Photo