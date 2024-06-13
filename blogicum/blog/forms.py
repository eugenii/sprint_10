from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from .models import Comment, Post

User = get_user_model()


class UserForm(forms.ModelForm):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = User
        # Указываем, что надо отобразить все поля.
        fields = ('first_name', 'last_name', 'username', 'email')


class PostForm(forms.ModelForm):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Post
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }
        # Указываем, что надо отобразить все поля.
        exclude = ('author',)


class CommentForm(forms.ModelForm):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Comment
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ('author',)

