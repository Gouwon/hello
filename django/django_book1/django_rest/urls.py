from rest_framework import (routers, renderers)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from django.urls import (path, include, re_path,)
from django.conf.urls import url

from . import views


app_name = 'django_rest'

snippet_list = views.SnippetViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
snippet_detail = views.SnippetViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)
snippet_highlight = views.SnippetViewSet.as_view(
    {
        'get': 'highlight'
    },
    renderer_classes =[
        renderers.StaticHTMLRenderer
    ]
)
user_list = views.UserViewSet.as_view(
    {
        'get': 'list',
    }
)
user_detail = views.UserViewSet.as_view(
    {
        'get': 'retrieve',
    }
)



urlpatterns = [
    path('snippets/', views.snippet_list, name='index'),
    path('snippets/<int:pk>/', views.snippet_detail, name='detail'),
    path('snippets/cls/', views.SnippetList.as_view(), name='cls_index'),
    path(
        'snippets/cls/<int:pk>/', views.SnippetDetail.as_view(), 
        name='cls_detail'
    ),
    path(
        'snippets/mxn/', views.SnippetListMixinExplicit.as_view(),
        name='mxn_index'
    ),
    path(
        'snippets/mxn/<int:pk>/', views.SnippetDetailMixinExplicit.as_view(),
        name='mxn_detail'
    ),
    path(
        'snippets/gv/', views.SnippetListMixin.as_view(), name='snippet_list'
    ),
    path(
        'snippets/gv/<int:pk>/', views.SnippetDetailMixin.as_view(),
        name='snippet_detail'
    ),

    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    path('', views.api_root, name='api'),
    path(
        'snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), 
        name='snippet_highlight'
    ),

    path(
        'snippets/vs/', snippet_list, name='vs_snippet_list'
    ),
    path(
        'snippets/vs/<int:pk>/', snippet_detail, name='vs_snippet_detail'
    ),
    path(
        'snippets/vs/<int:pk>/highlight/', snippet_highlight, 
        name='vs_snippet_highlight'
    ),
    path(
        'users/vs/', user_list, name='vs_user_list'
    ),
    path(
        'users/vs/<int:pk>/', user_detail, name='vs_user_detail'
    )
]

# defaultrouter also generates suffix for .json
router = DefaultRouter()
# router = DefaultRouter(trailing_slash=False)
router.register(r'snippets/router', views.SnippetViewSet)
router.register(r'users/router', views.UserViewSet)

urlpatterns.append(path('', include(router.urls)))

# adding prefix to existing urls with 
# urlpatterns = format_suffix_patterns(urlpatterns)