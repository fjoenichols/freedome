from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=False)
    join_date = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.username