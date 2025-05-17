from django import forms
from forum.models import Post, Thread

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'attachment', 'parent']
        labels = {
            'attachment': '',
        }
        widgets = {
            'parent': forms.HiddenInput(),
            'content': forms.Textarea(attrs={
                'placeholder': 'Напишіть відповідь...',
                'rows': 3,
                'class': 'reply-textarea',
                'style': 'resize: none; overflow: hidden;' 
            })
        }
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Повідомлення не може бути порожнім.")
        return content


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'placeholder': 'Напишіть короткий опис...',
                'rows': 2,
                'class': 'reply-textarea',
            })
        }

    