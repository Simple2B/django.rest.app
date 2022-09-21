from tabnanny import verbose
from django.db import models
# from profiles.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=64, null=False)
    content = models.CharField(max_length=512, null=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return f"<{self.id}: {self.title} at {self.created_at}>"

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = "posts"
