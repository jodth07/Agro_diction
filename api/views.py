from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer

from rest_framework_mongoengine import viewsets as meviewsets
from .serializers import ToolSerializer, BlogSerializer, PostSerializer
from .models import Tool, Blog, Post
 

class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class ToolViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class PostSerializerView(APIView):
    def get(self, request, post_id=None):

        if post_id is not None:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post, many=False)
            return Response(serializer.data)
        else:
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
        