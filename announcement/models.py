from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=36 )
    content = models.TextField()
    creator = models.ForeignKey(User , on_delete=models.DO_NOTHING, related_name="announcements")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title