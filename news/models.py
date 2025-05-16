from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="projects")
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
