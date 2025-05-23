from django import forms
from diary.models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student","grade"]