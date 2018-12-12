from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import Image, Gallery


class ImageSerializer(EmbeddedDocumentSerializer):
    
    class Meta:
        model = Image
        exclude = ()


class GallerySerializer(EmbeddedDocumentSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        exclude = ()