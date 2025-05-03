from django import forms
from .models import Choice

class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None
    )

    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = poll.choices.all()