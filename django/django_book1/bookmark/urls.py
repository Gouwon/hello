from django.urls import path

from . import views


app_name = 'bookmark'

urlpatterns = [
    path('', views.BookmarkListView.as_view(), name='index'),
    path('<int:pk>', views.BookmarkDetailView.as_view(), name='detail'),
]