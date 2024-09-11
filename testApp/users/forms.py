from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(AuthenticationForm):
    pass
