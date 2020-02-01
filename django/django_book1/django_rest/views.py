from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, JsonResponse)

from .models import Snippet
from .serializers import SnippetModelSerializer
from programmers_test.views import resonpse_in_json


# Create your views here.
@csrf_exempt
@resonpse_in_json
def snippet_list(request):
    """
    list all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return serializer.data
    
    elif requeset.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

@csrf_exempt
@resonpse_in_json
def snippet_detail(request, pk):
    """
    retrieve, update or delete a code snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist as sqlerr:
        print('\n\n\n snippet_detail sqlerr >>>>> ', sqlerr)
        return {'status': 404}
    
    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        return serializer.data
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors
    
    elif request.method == 'DELETE':
        snippet.delete()
        return {'status': 204}