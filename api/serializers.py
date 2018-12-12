from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import Tool, Post, User, Blog, BlogExtension, Comment

class ToolSerializer(DocumentSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class CommentSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Comment
        
class ExtensionSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = BlogExtension

class BlogSerializer(DocumentSerializer):
    extension = ExtensionSerializer(many=False)

    class Meta:
        model = Blog

class PostSerializer(DocumentSerializer):
    comments = CommentSerializer(many=True)
    extension = ExtensionSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'blog', 'author', 'text', 'comments', 'extension')
        depth = 2

    def update(self, instance, validated_data):
        comments = validated_data.pop('comments')
        updated_instance = super(PostSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            updated_instance.comments.append(Comment(**comment_data))

        updated_instance.save()
        return updated_instance