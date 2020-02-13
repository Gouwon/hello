from django.urls import (path, re_path)

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    re_path(
        r'^post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), 
        name='post_detail'
    ),   
    path('archive/', views.PostArchiveView.as_view(), name='post_archive'),
    path(
        'archive/<int:year>/', views.PostYearArchiveView.as_view(),
        name='post_year_archive'
    ),
    path(
        'archive/<int:year>/<str:month>/', 
        views.PostMonthArchiveView.as_view(), 
        name='post_month_archive'
    ),
    path(
        'archive/<int:year>/<str:month>/<int:day>/', 
        views.PostDayArchiveView.as_view(), 
        name='post_day_archive'
    ),
    path(
        'archive/today/', views.PostTodayArchiveView.as_view(), 
        name='post_today_archive'
    ),
    path(
        'tag/', views.TagCloudTemplateView.as_view(), name='tag_cloud'
    ),
    path(
        'tag/<str:tag>/', views.TaggedObjectListView.as_view(), 
        name='tagged_object_list'
    ),
    path(
        'search/', views.SearchFormView.as_view(), name='search'
    ),
]