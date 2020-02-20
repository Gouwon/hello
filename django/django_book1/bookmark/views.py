from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bookmark
from django_pjt.views import OwnerOnlyMixin


# Create your views here.
class BookmarkListView(generic.ListView):
    model = Bookmark

class BookmarkDetailView(generic.DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bookmark
    fields = [
        'title', 'url', 
    ]
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, generic.UpdateView):
    model = Bookmark
    fields = [
        'title', 'url', 
    ]
    suceess_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, generic.DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')