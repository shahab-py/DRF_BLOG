from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
class CommentView(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    