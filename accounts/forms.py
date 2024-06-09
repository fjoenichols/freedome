from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100, required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    github_link = forms.URLField(required=False)
    avatar = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'password1', 'password2', 'bio', 'github_link', 'avatar']