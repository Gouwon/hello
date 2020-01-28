from django.urls import path
from . import views


app_name = 'programmers_test'
extra_patterns = [
    path('a', views.pindex, name='pindex'),
    path('<int:id>', views.ItemView.as_view(), name='details'),
]

urlpatterns = [
    path('', views.ItemListView.as_view(), name='lists'),
]
