"""django_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import (handler403, handler404, handler500)

import django_app   #NOQA
import django_rest  #NOQA
from programmers_test import urls as p_urls
from programmers_test.views import (error403, error404, error500)
from books.views import HomeView
import bookmark
import blog
import photo
from .views import (UserCreateView, UserCreateDoneTemplateView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('django_app.urls')),
    path('rest/', include('django_rest.urls')),
    re_path(r'^product\/', include((p_urls.extra_patterns, 'programmers_test')), name='product'),
    re_path(r'^products', include((p_urls.urlpatterns, 'programmers_test')), name='products'),
    path('books/', include('books.urls')),
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),  # for adding login to the browsable api
    path('photo/', include('photo.urls')),
    path(
        'accounts/', include('django.contrib.auth.urls')
    ),
    path(
        'accounts/register/', UserCreateView.as_view(), name='register'
    ),
    path(
        'accounts/register/done/', UserCreateDoneTemplateView.as_view(),
        name='register_done'
    ), 
]

# defaults.page_not_found(request, exception, template_name='404.html')
handler403 = error403
handler404 = error404
handler500 = error500

