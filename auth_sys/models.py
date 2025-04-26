from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Portfolio(models.Model):
    class Permissions(models.TextChoices):
        ADMIN = "ADMIN", "administrator"
        MODER = "MODER", "moderator"
        STUDENT = "STUDENT", "student"
        USER = "USER", "user"

    image = models.ImageField(upload_to="auth_sys/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    birthday_day = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="portfolio")
    permission = models.CharField(max_length=15, choices=Permissions.choices,
                                  default=Permissions.USER)

    def __str__(self):
        return self.user.username

    def years_old(self):
        return (datetime.now() - self.birthday_day).years

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"
