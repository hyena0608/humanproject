from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import CustomUser
from django import forms
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'body', 'email']
        help_texts = {
            'username': None,
        }