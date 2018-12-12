# words.views

from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Definition, Antonym, Synonym, Word 
from .serializers import DefinitionSerializer, AntonymSerializer, SynonymSerializer, WordSerializer

class WordView(APIView):
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

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : WordSerializer(many=True)}
    )
    def get(self, request, word_id=None):
        if word_id is not None:
            word = Word.objects.get(id=word_id)
            serializer = WordSerializer(word, context={"request": request}, many=True)
            return Response(serializer.data)
        else:
            words = Word.objects.all()
            serializer = WordSerializer(words, context={"request": request}, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=WordSerializer,
        responses={
            status.HTTP_200_OK : WordSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request, *args, **kwargs):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, word_id):
    
        word = Word.objects.get(id=word_id)
        word.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : WordSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, word_id):
        
        word = Word.objects.get(id=word_id)
        
        serializer = WordSerializer(word, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


