from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.slug})
    
    
    
    
    