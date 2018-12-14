# images.views

from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Image, Gallery 
from .serializers import ImageSerializer, GallerySerializer

class GallerysView(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer