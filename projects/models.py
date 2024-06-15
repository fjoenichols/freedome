from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Project, on_delete=models.CASCADE)

class Subtask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)

class TaskComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)