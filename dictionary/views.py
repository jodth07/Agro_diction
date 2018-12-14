# words.views

from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Definition, Antonym, Synonym, Word 
from .serializers import DefinitionSerializer, AntonymSerializer, SynonymSerializer, WordSerializer

class WordView(viewsets.ModelViewSet):
    """
    get:
    Return a list of all existing words/words 
    
    post:
    Add new Word
    
    put:
    Update a contact
    
    delete:
    Delete an word
    """

    permission_classes = (AllowAny,)

    lookup_field = 'id'
    queryset = Word.objects.all()
    serializer_class = WordSerializer



