from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlparse


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255)
    form = models.CharField(max_length=155, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                              related_name="subjects")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "subject"
        verbose_name_plural = "subjects"


class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name="materials")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materials"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="material_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE,
                                 related_name="comments")

    def __str__(self):
        return f"{self.author} at {self.created_at}"

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"


class Investment(models.Model):
    media = models.FileField(upload_to="materials/", null=True, blank=True)
    adress = models.URLField(null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE,
                                 related_name="investments")

    def is_youtube(self):
        site = urlparse(self.adress)[1]
        return (site == "youtu.be" or site == "www.youtube.com")

    def get_youtube_scr(self):
        match urlparse(self.adress)[1]:
            case "youtu.be":
                return urlparse(self.adress)[2][1:]
            case "www.youtube.com":
                return urlparse(self.adress)[4].split("=")[1]

    def __str__(self):
        return f"{self.media}{self.adress}"

    class Meta:
        verbose_name = "investment"
        verbose_name_plural = "investments"
