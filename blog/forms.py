from .models import Comment
from django import forms
from about.models import CollaborateRequest 



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)