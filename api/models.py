from rest_framework import serializers
from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, StringField, ReferenceField, ListField, DictField, EmailField, DynamicDocument,  BooleanField, EmbeddedDocumentField 

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()



class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)
 
class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))


class User(Document):
    username = StringField(max_length=30)
    email = EmailField(max_length=30)
    friends = ListField(ReferenceField('self'))
    extra = DictField()

class BlogExtension(EmbeddedDocument):
    further_read = StringField(required=True)
    references = ListField(StringField())

class Blog(DynamicDocument):
    owner = ReferenceField(User)
    title = StringField(max_length=30)
    tags = ListField(StringField())

class Comment(EmbeddedDocument):
    author = ReferenceField(User)
    text = StringField(max_length=140)
    is_approved = BooleanField(default=False)

class Post(Document):
    author = ReferenceField(User)
    blog = ReferenceField(Blog)
    text = StringField()
    comments = ListField(EmbeddedDocumentField(Comment))
    extension = EmbeddedDocumentField(BlogExtension)