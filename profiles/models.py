from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    username = models.CharField(max_length=60, unique=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"
