from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=50, default='Python')
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name