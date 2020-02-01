from rest_framework import routers
from django.urls import (path, include, re_path,)
from django.conf.urls import url
from . import views


app_name = 'django_rest'

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]