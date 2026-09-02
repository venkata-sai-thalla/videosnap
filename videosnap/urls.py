from django.contrib import admin
from django.urls import path, include
from accounts import views   # Import home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("", include('accounts.urls')),
    path("posts/", include('posts.urls')),
    path("videos/", include('videos.urls')),
    path("products/", include('products.urls')),
]
