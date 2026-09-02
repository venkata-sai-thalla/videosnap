from django import forms
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/uploaded/', blank=True, null=True)

    def __str__(self):
        return self.name

class ChatBot(models.Model):
    user_input=models.TextField()
    text_output=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input

class ChatHistory(models.Model):
    user_input=models.TextField()
    text_output=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input
    