from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="portfolio")
