from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.posts_view, name="post"),
    path("create-post/", views.create_post_view, name="create-post"),
    
]