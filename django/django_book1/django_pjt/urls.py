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
from django.contrib import admin
from django.urls import path, include, re_path
import django_app   #NOQA
import django_rest  #NOQA
from django.conf.urls import (handler403, handler404, handler500)

from programmers_test import urls as p_urls
from programmers_test.views import (error403, error404, error500)
from books.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('django_app.urls')),
    path('sss/', include('django_rest.urls')),
    re_path(r'^product\/', include((p_urls.extra_patterns, 'programmers_test')), name='product'),
    re_path(r'^products', include((p_urls.urlpatterns, 'programmers_test')), name='products'),
    path('books/', include('books.urls')),
    path('', HomeView.as_view(), name='home'),
]

# defaults.page_not_found(request, exception, template_name='404.html')
handler403 = error403
handler404 = error404
handler500 = error500

