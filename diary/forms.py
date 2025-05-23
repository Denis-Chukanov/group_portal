from django import forms
from diary.models import Grade , Subject

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student","grade"]

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["title", "students"]