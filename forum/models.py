from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Thread(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(default="No content")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(
        upload_to='attachments/', 
        blank=True, 
        null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'png', 'jpg', 'jpeg'])]
    )

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(
        upload_to='attachments/', 
        blank=True, 
        null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'png', 'jpg', 'jpeg'])]
    )
    