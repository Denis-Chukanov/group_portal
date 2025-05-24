from django.forms import ModelForm
from materials import models


class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ("content", )

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        content_field = self.fields["content"].widget.attrs
        content_field.update({"rows": 4, "cols": 50,
                              "class": "content", })


class SubjectForm(ModelForm):
    class Meta:
        model = models.Subject
        fields = ("name", "form", )


class MaterialForm(ModelForm):
    class Meta:
        model = models.Material
        fields = ("name", "description", "subject", )

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        description_field = self.fields["description"].widget.attrs
        description_field.update({"class": "content",
                                  "id": "content"})
