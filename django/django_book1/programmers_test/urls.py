from rest_framework.routers import DefaultRouter

from django.urls import (path, include)

from . import views


app_name = 'programmers_test'
extra_patterns = [
    path('a', views.index, name='index'),
    path('<int:id>', views.ItemView.as_view(), name='details'),
]

urlpatterns = [
    path('', views.ItemListAPIView.as_view(), name='lists'),
]

router = DefaultRouter()
router.register(r'', views.ItemListAPIView)

urlpatterns.append(path('', include(router.urls)))