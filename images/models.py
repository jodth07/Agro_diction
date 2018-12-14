# images.models

from datetime import datetime 
# from drf_base64.fields import Base64ImageField
from mongoengine import Document, EmbeddedDocument, fields


class Image(EmbeddedDocument):
    image = fields.FileField()
    name = fields.StringField(max_length=100)

class Gallery(Document):
    name = fields.StringField(max_length=100)
    images = fields.ListField(fields.EmbeddedDocumentField(Image))
    updated = fields.StringField(max_length=100)

