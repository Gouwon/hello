from django.urls import path
from django_test import views

urlpatterns = [ path("", views.home, name="home"), ]