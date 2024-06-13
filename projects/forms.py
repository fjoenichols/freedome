from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Project
        fields = ['title', 'description']