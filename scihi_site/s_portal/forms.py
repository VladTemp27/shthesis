from django import forms
from django.forms import ModelForm
from django import forms
from .models import Student
from django.contrib.auth.hashers import make_password

class RegisterForm(ModelForm):
    username = forms.TextInput
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['username', 'password']
