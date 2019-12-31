from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'username', 'placeholder': 'Username', 'id': 'name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'name': 'username',
            'placeholder': 'Password',
            'id': 'password',
        }
    ))
