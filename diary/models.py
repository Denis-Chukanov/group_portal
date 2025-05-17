from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=30)
    students = models.ManyToManyField(User, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="creator")

    def __str__(self):
        return self.title

class Grade(models.Model):
    GRADE_CHOICES = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("11", 11),
        ("12", 12),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="10")
    date = models.DateTimeField()

    def __str__(self):
        return self.grade