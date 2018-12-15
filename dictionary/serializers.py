from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import Definition, Synonym, Antonym, Word

class DefinitionSerializer(EmbeddedDocumentSerializer):
    
    class Meta:
        model = Definition
        exclude = ()


class SynonymSerializer(EmbeddedDocumentSerializer):
    
    class Meta:
        model = Synonym
        exclude = ()


class AntonymSerializer(EmbeddedDocumentSerializer):
    
    class Meta:
        model = Antonym
        exclude = ()


class WordSerializer(DocumentSerializer):
    # definitions = DefinitionSerializer(many=True)
    # synonyms = SynonymSerializer()
    # antonyms = AntonymSerializer()
    
    class Meta:
        model = Word
        exclude = ()

