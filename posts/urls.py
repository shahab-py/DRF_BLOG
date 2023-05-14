from django.urls import path

from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_details'),
    path('comments/<int:pk>/', views.CommentView.as_view(), name='comments'),
    path('upvotes/<int:pk>/', views.UpVoteView.as_view(), name='vpvotes'),
]