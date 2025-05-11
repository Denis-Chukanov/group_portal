from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlparse
from django.templatetags.static import static


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
    changed_at = models.DateTimeField(auto_now_add=True)

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
        ordering = ("-created_at", )
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

    def get_domen(self):
        return urlparse(self.adress)[1]

    def get_filename(self):
        return self.media.name.split("/")[-1]

    def get_image(self):
        format_to_image = {
            "pdf": static("img/pdf.png"),
            "mp4": static("img/video.png"),
            "webm": static("img/video.png"),
            "mp3": static("img/audio.png"),
            "wav": static("img/audio.png"),
            "ogg": static("img/audio.png"),
            "jpg": static("img/photo.jpg"),
            "jpeg": static("img/photo.jpg"),
            "png": static("img/photo.jpg"),
            "gif": static("img/photo.jpg"),
            "webp": static("img/photo.jpg"),
            "txt": static("img/txt.png"),
        }
        filetype = self.media.name.split(".")[-1].lower()
        try:
            return format_to_image[filetype]
        except:
            return static("img/code.png")

    def __str__(self):
        return f"{self.media}{self.adress}"

    class Meta:
        verbose_name = "investment"
        verbose_name_plural = "investments"
