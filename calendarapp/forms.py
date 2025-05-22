from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time']
        widgets = {
            'start_time': forms.TextInput(attrs={'id': 'datePicker'}),
        }
