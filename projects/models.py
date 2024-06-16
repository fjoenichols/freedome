from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AbstractTask(models.Model):
    STATUS_CHOICES = ( 
        ("Backlog", "Backlog"), 
        ("To Do", "To Do"), 
        ("In Progress", "In Progress"), 
        ("In Review", "In Review"), 
        ("Done", "Done"), 
        ("Cancelled", "Cancelled"), 
    ) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField( 
        max_length = 20, 
        choices = STATUS_CHOICES, 
        default = 'Backlog'
        ) 
    due_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Task(AbstractTask):
    parent = models.ForeignKey("Project", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Subtask(AbstractTask):
    parent = models.ForeignKey("Task", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class AbstractComment(models.Model):
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class ProjectComment(AbstractComment):
    parent = models.ForeignKey("Project", on_delete=models.CASCADE)

class TaskComment(AbstractComment):
    parent = models.ForeignKey("Task", on_delete=models.CASCADE)

class SubtaskComment(AbstractComment):
    parent = models.ForeignKey("Subtask", on_delete=models.CASCADE)