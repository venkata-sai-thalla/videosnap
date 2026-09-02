from django.db import models
from accounts.models import Profile

class Video(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to="videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"

