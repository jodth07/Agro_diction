# dictionary.models

# from django.db import models
from rest_framework import serializers
from datetime import datetime 
# from drf_base64.fields import Base64ImageField
from mongoengine import Document, EmbeddedDocument, fields


class Definition(EmbeddedDocument):
    definition = fields.StringField(max_length=250)
    example  = fields.StringField(max_length=250)

class Synonym(EmbeddedDocument):
    synonym = fields.StringField(max_length=250)

class Antonym(EmbeddedDocument):
    antonym = fields.StringField(max_length=250)   

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
    
    views = fields.StringField(max_length=250)
    searched = fields.StringField(max_length=250)
   
    is_defined = fields.StringField(max_length=250)
    define_date = fields.StringField(max_length=250)
    definer = fields.StringField(max_length=250)

    is_revised = fields.StringField(max_length=250)    
    revised_date = fields.StringField(max_length=250)   
    revise = fields.StringField(max_length=250)
    
    is_published = fields.StringField(max_length=250)    
    published_date = fields.StringField(max_length=250)    
    publisher = fields.StringField(max_length=250)

    is_visible = fields.StringField(max_length=250)

