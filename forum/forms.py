from django import forms
from forum.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'attachment', 'parent']
        widgets = {
            'parent': forms.HiddenInput(),
            'content': forms.TextInput(attrs={'placeholder': 'Напишіть відповідь...'})
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Повідомлення не може бути порожнім.")
        return content