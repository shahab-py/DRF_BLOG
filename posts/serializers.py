from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')
        read_only_fields = ('created_at',)
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at')
        read_only_fields = ('created_at',)
