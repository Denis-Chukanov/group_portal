from django.db import models
from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(default="")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False, default="")
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title