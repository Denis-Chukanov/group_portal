from django.forms import ModelForm
from materials import models


class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ("content", )


class SubjectForm(ModelForm):
    class Meta:
        model = models.Subject
        fields = ("name", "form", )


class MediaForm(ModelForm):
    class Meta:
        model = models.Investment
        fields = ("media", )

    def __init__(self):
        media_field = self.fields["media"].widget.attrs
        media_field.update({"required": ""})


class AdressForm(ModelForm):
    class Meta:
        model = models.Investment
        fields = ("adress", )

    def __init__(self):
        media_field = self.fields["adress"].widget.attrs
        media_field.update({"required": ""})
