from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import (path, include, re_path,)
from django.conf.urls import url

from . import views


app_name = 'django_rest'

urlpatterns = [
    path('snippets/', views.snippet_list, name='index'),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/cls/', views.SnippetList.as_view()),
    path('snippets/cls/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/mxn/', views.SnippetListMixinExplicit.as_view()),
    path('snippets/mxn/<int:pk>/', views.SnippetDetailMixinExplicit.as_view()),
    path('snippets/gv/', views.SnippetListMixin.as_view()),
    path('snippets/gv/<int:pk>/', views.SnippetDetailMixin.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
]

# adding prefix to existing urls with 
urlpatterns = format_suffix_patterns(urlpatterns)