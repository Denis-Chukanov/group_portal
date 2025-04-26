from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from auth_sys.models import Portfolio
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "email",)


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ("image", "description", "birthday_day")
        widgets = {
            "birthday_day": forms.DateInput(attrs={"type": "date"}),
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
