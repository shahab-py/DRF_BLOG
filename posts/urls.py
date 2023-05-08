from django.urls import path

from . import views


app_name = 'posts'


urlpatterns = [
    path('posts/', views.PostView.as_view(), name='posts'),
]