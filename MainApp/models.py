from django.db import models
from django.contrib.auth.models import User



class Snippet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title