from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    done = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)
    date_limit = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
