from django import forms
from django.contrib.auth.models import User
from .models import Resource
from django.contrib.auth.forms import UserCreationForm

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

