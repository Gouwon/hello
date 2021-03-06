from django.urls import path

from . import views


app_name = 'bookmark'

urlpatterns = [
    path('', views.BookmarkListView.as_view(), name='index'),
    path('<int:pk>', views.BookmarkDetailView.as_view(), name='detail'),
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeListView.as_view(), name='change'),
    path(
        '<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'
    ),
    path(
        '<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'
    ), 
]