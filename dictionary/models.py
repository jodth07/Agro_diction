# dictionary.models

# from django.db import models
from rest_framework import serializers
from datetime import datetime 
# from drf_base64.fields import Base64ImageField
from mongoengine import Document, EmbeddedDocument, fields
from users.models import Editor


class Definition(EmbeddedDocument):
    definition = fields.StringField(max_length=250)
    example  = fields.StringField(max_length=250)

class Synonym(EmbeddedDocument):
    synonym = fields.ReferenceField('Word')

class Antonym(EmbeddedDocument):
    antonym = fields.ReferenceField('Word')   

class Word(Document):
   
    common_name = fields.StringField(max_length=250)
    name = fields.StringField(max_length=250)
    other_names = fields.ListField(fields.StringField(max_length=250))
    scientific_name = fields.StringField(max_length=250)
    family = fields.StringField(max_length=250)

    origin = fields.StringField(max_length=250)

    category = fields.StringField(max_length=250)
    sub_category = fields.StringField(max_length=250)
    tags = fields.ListField(fields.StringField(max_length=250))

    definitions = fields.ListField(fields.EmbeddedDocumentField(Definition))
    short_description = fields.StringField(max_length=250)
    description = fields.StringField(max_length=250)
    synonyms = fields.ListField(fields.EmbeddedDocumentField(Synonym))
    antonyms = fields.ListField(fields.EmbeddedDocumentField(Antonym))
    
    other_info = fields.StringField(max_length=250)
    
    source = fields.StringField(max_length=250)
    
    views = fields.IntField()
    searched = fields.IntField()
   
    is_defined = fields.BooleanField(default=True)
    define_date = fields.StringField(max_length=250)
    definer = fields.ReferenceField(Editor)

    is_revised = fields.BooleanField(default=False) 
    revised_date = fields.StringField(max_length=250)   
    reviser = fields.ReferenceField(Editor)
    
    is_published = fields.BooleanField(default=False)   
    published_date = fields.StringField(max_length=250)    
    publisher = fields.ReferenceField(Editor)

    is_visible = fields.BooleanField(default=False)

