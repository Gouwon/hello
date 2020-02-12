from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .models import Post
from .forms import PostSearchForm


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(generic.DetailView):
    model = Post

class PostArchiveView(generic.ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYearArchiveView(generic.YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMonthArchiveView(generic.MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDayArchiveView(generic.DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTodayArchiveView(generic.TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTemplateView(generic.TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectListView(generic.ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

class SearchFormView(generic.FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search = form.cleaned_data['search']
        post_list = Post.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search) | 
            Q(content__icontains=search)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)