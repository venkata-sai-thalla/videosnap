from django import forms
from .models import ChatHistory

class ChatHistoryForm(forms.ModelForm):
    class Meta:
        model = ChatHistory
        fields = ['user_input']
