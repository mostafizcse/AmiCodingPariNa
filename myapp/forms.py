from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
        ]
