from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    done = models.BooleanField(default=False)
    complete_before = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
