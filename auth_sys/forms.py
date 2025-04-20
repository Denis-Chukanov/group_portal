from django.forms import Form, ModelForm
from django.contrib.auth import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = forms.UserCreationForm.Meta.fields + ("first_name",
                                                       "last_name",
                                                       "email",)


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
