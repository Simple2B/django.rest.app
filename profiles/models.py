from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class UserProfile(AbstractUser):
    username = models.CharField(max_length=60, unique=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    @property
    def password_hash(self):
        return make_password(self.password)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"
