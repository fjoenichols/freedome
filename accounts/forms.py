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

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            try:
                if visible.field.widget.input_type == 'text':
                    visible.field.widget.attrs['class'] = 'input'
                elif visible.field.widget.input_type == 'email':
                    visible.field.widget.attrs['class'] = 'input'
                elif visible.field.widget.input_type == 'password':
                    visible.field.widget.attrs['class'] = 'input'
                elif visible.field.widget.input_type == 'url':
                    visible.field.widget.attrs['class'] = 'input'
                elif visible.field.widget.input_type == 'file':
                    visible.field.widget.attrs['class'] = 'button'
            except AttributeError:
                visible.field.widget.attrs['class'] = 'textarea'
