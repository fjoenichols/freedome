from django import forms
from .models import Project

from .models import Task, Subtask
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Project
        fields = ['title', 'description']
STATUS_CHOICES = ( 
    ("Backlog", "Backlog"), 
    ("To Do", "To Do"), 
    ("In Progress", "In Progress"), 
    ("In Review", "In Review"), 
    ("Done", "Done"), 
    ("Cancelled", "Cancelled"), 
) 

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    due_date = forms.DateField(required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']

class SubtaskForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    due_date = forms.DateField(required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Subtask
        fields = ['title', 'description', 'status', 'due_date']