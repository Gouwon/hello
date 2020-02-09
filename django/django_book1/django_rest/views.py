from rest_framework import (
    status, mixins, generics, permissions, renderers, viewsets
)
from rest_framework.parsers import JSONParser
from rest_framework.decorators import (api_view, APIView, action)
from rest_framework.reverse import reverse
from rest_framework.response import Response

from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, JsonResponse, Http404)
from django.contrib.auth.models import User

from .models import Snippet
from .serializers import (
    SnippetModelSerializer, UserSerializer, SnippetHTMLModelSerializer,
    UserHTMLModelSerializer, 
)
from programmers_test.views import resonpse_in_json
from .permissions import IsOwnerOrReadOnly


# don't need to give content type when accessing to data. 
# request.data can handle json request by default.

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse(
                'django_rest:user_list', request=request, format=format
            ),
            'snippets': reverse(
                'django_rest:snippet_list', request=request, format=format
            )
        }
    )

class SnippetHighlight(generics.GenericAPIView):    
    queryset = Snippet.objects.all()
    renderer_classes = [
        renderers.StaticHTMLRenderer, 
    ]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlisted)

@csrf_exempt
@api_view(['GET', 'POST'])
# @resonpse_in_json
def snippet_list(request, format=None):
    """
    list all code snippets, or create a new snippet
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        # serializer = SnippetHTMLModelSerializer(
        #     snippets, many=True, context={'request': request}
        # )
        # return serializer.data
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = SnippetModelSerializer(data=data)
        # serializer = SnippetModelSerializer(data=request.data)
        serializer = SnippetHTMLModelSerializer(
            data=request.data, context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            # return serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
# @resonpse_in_json
def snippet_detail(request, pk, format=None):
    """
    retrieve, update or delete a code snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist as sqlerr:
        print('\n\n\n snippet_detail sqlerr >>>>> ', sqlerr)
        # return {'status': 404}
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        # serializer = SnippetHTMLModelSerializer(snippet)
        # return serializer.data
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        # serializer = SnippetModelSerializer(snippet, data=data)
        serializer = SnippetModelSerializer(snippet, data=request.data)
        # serializer = SnippetHTMLModelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return serializer.data
            return Response(serializer.data)
        # return serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        # return {'status': 204}
        return Response(status=status.HTTP_204_NO_CONTENT)

# class-based view

class SnippetList(APIView):
    """
    list all snippets, or create a new snippet
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        # serializer = SnippetModelSerializer(snippets, many=True)
        serializer = SnippetHTMLModelSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # serializer = SnippetModelSerializer(data=request.data)
        serializer = SnippetHTMLModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    retrieve, update or delete a snippet instance
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        # serializer = SnippetModelSerializer(snippet)
        serializer = SnippetHTMLModelSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        # serializer = SnippetModelSerializer(snippet, data=request.data)
        serializer = SnippetHTMLModelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# using Mixin class
class SnippetListMixinExplicit(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, 
):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetModelSerializer
    serializer_class = SnippetHTMLModelSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetailMixinExplicit(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, generics.GenericAPIView, 
):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetModelSerializer
    serializer_class = SnippetHTMLModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SnippetListMixin(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetModelSerializer
    serializer_class = SnippetHTMLModelSerializer
    print('\n\n\n SnippetListMixinSnippetListMixin >>>>> ', serializer_class)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsOwnerOrReadOnly, 
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetailMixin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    # serializer_class = SnippetModelSerializer
    serializer_class = SnippetHTMLModelSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,  
    ]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    this viewset automatically provides list and detail actions
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    this viewset automatically provides list, create, retrieve, update, and 
    destroy actions.
    additionally adding an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetHTMLModelSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlisted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)