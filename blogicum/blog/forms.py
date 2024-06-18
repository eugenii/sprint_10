from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from .models import Comment, Post

User = get_user_model()


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PostForm(forms.ModelForm):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Post
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ('author',)


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',) 

