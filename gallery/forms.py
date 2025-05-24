from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    title = forms.CharField(required=False)
    content = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.ImageField(required=True)
    class Meta:
        model = Image
        fields = ['title', 'content', 'image']
        