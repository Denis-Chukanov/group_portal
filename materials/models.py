from django.db import models
from django.contrib.auth.models import User


# data-popup="yes"
# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                              related_name="materials")

    def __str__(self):
        return self.name
