from django.db import models
from django.conf import settings
from django.urls import reverse



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.content[:15]}'
    
    
    
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.slug})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user} - {self.content[:20]}'