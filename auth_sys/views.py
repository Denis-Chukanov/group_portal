from django.shortcuts import render, redirect
from django.contrib.auth import views
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from auth_sys.forms import UserCreationForm, UserUpdateForm, PortfolioForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from auth_sys.models import Portfolio


# Create your views here.
def user_creation(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        portfolio_form = PortfolioForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if portfolio_form.is_valid():
                portfolio = portfolio_form.save(commit=False)
                portfolio.user = user
                user.save()
                portfolio.save()
                login(request, user)
                return redirect("main_page")

        else:
            messages.error(request, user_form.errors)
            messages.error(request, portfolio_form.errors)

    template_name = "auth_sys/user_create_form.html"
    context = {
        "form": UserCreationForm,
        "portfolio_form": PortfolioForm,
    }
    return render(request,
                  template_name,
                  context)


@login_required
def user_update(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.pk)
        portfolio = Portfolio.objects.get(user=user)
        user_form = UserUpdateForm(request.POST)
        portfolio_form = PortfolioForm(request.POST, request.FILES)
        portfolio_form.Meta.set_value(portfolio)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            if portfolio_form.is_valid():
                new_portfolio = portfolio_form.save(commit=False)
                new_portfolio.user = new_user
                new_user.save()
                new_portfolio.save()
                return redirect("main_page")

        else:
            messages.error(request, user_form.errors)
            messages.error(request, portfolio_form.errors)

    template_name = "auth_sys/user_update_form.html"
    context = {
        "form": UserUpdateForm,
        "portfolio_form": PortfolioForm,
    }
    return render(request,
                  template_name,
                  context)


def user_details(request, pk):
    user = User.objects.get(id=pk)
    portfolio = Portfolio.objects.get(user=user)
    context = {
        "user": user,
        "portfolio": portfolio,
    }
    return render(request,
                  "auth_sys/user_details.html",
                  context=context)


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


class CustomLoginMenuView(views.LoginView):
    template_name = "auth_sys/user_login_menu.html"