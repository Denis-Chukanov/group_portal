from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    max_comments = models.PositiveIntegerField(
        default=10,
        help_text="Сколько ответов принимается, прежде чем опрос закрыт"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_closed(self):
        return self.comments.count() >= self.max_comments

class SurveyComment(models.Model):
    survey = models.ForeignKey(Survey, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.survey.title}'

    @property
    def likes(self):
        return self.liked_by.count()
