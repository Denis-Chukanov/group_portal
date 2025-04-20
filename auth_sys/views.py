from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from auth_sys.forms import UserCreationForm, UserUpdateForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserCreationView(CreateView):
    model = User
    template_name = "auth_sys/user_create_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("main_page")

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "auth_sys/user_update_form.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("main_page")

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordUpdateView(LoginRequiredMixin, views.PasswordChangeView):
    success_url = reverse_lazy("main_page")
    template_name = "auth_sys/user_update_form.html"


class CustomLoginView(views.LoginView):
    success_url = reverse_lazy("main_page")
    template_name = "auth_sys/user_login_form.html"


class CustomUserDeleteView(DeleteView):
    model = User
    template_name = "auth_sys/user_delete_form.html"
    success_url = reverse_lazy("register")

    def get_object(self, queryset=None):
        return self.request.user
