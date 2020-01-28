from rest_framework import routers
from django.urls import (path, include, re_path,)
from django.conf.urls import url
from . import views

app_name = 'django_rest'
router = routers.DefaultRouter()
router.register(r'vvv/', views.ItemViewSet)
# router.register(r'vvv/', views.ItemView.as_view())

urlpatterns = [
    path(r'xxx', views.ItemView.as_view()),
    url(r'^', include(router.urls), name='basic'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]