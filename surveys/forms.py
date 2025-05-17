from django import forms
from .models import SurveyComment

class SurveyCommentForm(forms.ModelForm):
    class Meta:
        model = SurveyComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }