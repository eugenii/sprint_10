from django import forms
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = User
        # Указываем, что надо отобразить все поля.
        fields = ('first_name', 'last_name', 'username', 'email')