from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=200)  # Добавьте это поле
    description = models.TextField(blank=True, null=True)  # И это поле
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
