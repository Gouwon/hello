from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import (path, include, re_path,)
from django.conf.urls import url

from . import views


app_name = 'django_rest'

urlpatterns = [
    path('snippets/', views.snippet_list, name='index'),
    path('snippets/<int:pk>/', views.snippet_detail, name='detail'),
    path('snippets/cls/', views.SnippetList.as_view(), name='cls_index'),
    path(
        'snippets/cls/<int:pk>/', views.SnippetDetail.as_view(), 
        name='cls_detail'
    ),
    path(
        'snippets/mxn/', views.SnippetListMixinExplicit.as_view(),
        name='mxn_index'
    ),
    path(
        'snippets/mxn/<int:pk>/', views.SnippetDetailMixinExplicit.as_view(),
        name='mxn_detail'
    ),
    path(
        'snippets/gv/', views.SnippetListMixin.as_view(), name='snippet_list'
    ),
    path(
        'snippets/gv/<int:pk>/', views.SnippetDetailMixin.as_view(),
        name='snippet_detail'
    ),

    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    path('', views.api_root, name='api'),
    path(
        'snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), 
        name='snippet_highlight'
    ),
]

# adding prefix to existing urls with 
urlpatterns = format_suffix_patterns(urlpatterns)