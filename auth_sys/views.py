from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from auth_sys.forms import UserCreationForm, UserUpdateForm, PortfolioForm
from django.contrib.auth import login, logout
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
                return redirect("news_list")

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
    user = User.objects.get(pk=request.user.pk)
    try:
        portfolio = Portfolio.objects.get(user=user)
    except Portfolio.DoesNotExist:
        portfolio = Portfolio(user=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        portfolio_form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        
        if user_form.is_valid() and portfolio_form.is_valid():
            user_form = user_form.save()    
            portfolio_form = portfolio_form.save(commit=False)
            portfolio_form.user = request.user
            portfolio_form.save()
            login(request, user_form)
            return redirect("news_list")
        else:
            messages.error(request, user_form.errors)
            messages.error(request, portfolio_form.errors)

    template_name = "auth_sys/user_update_form.html"
    context = {
        "form": UserUpdateForm(instance=user),
        "portfolio_form": PortfolioForm(instance=portfolio),
    }
    return render(request,
                  template_name,
                  context)


def user_details(request, pk):
    user_obj = get_object_or_404(User, id=pk)
    portfolio = get_object_or_404(Portfolio, user=user_obj)
    context = {
        "viewed_user": user_obj,    
        "portfolio": portfolio,
    }
    return render(request,
                  "auth_sys/user_details.html",
                  context=context)


def request_user_details(request):
    user = User.objects.get(id=request.user.pk)
    portfolio = Portfolio.objects.get(user=user)
    context = {
        "user": user,
        "portfolio": portfolio,
    }
    return render(request,
                  "auth_sys/request_user_details.html",
                  context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


class UserPasswordUpdateView(LoginRequiredMixin, views.PasswordChangeView):
    success_url = reverse_lazy("news_list")
    template_name = "auth_sys/user_password_update_form.html"


class CustomLoginView(views.LoginView):
    template_name = "auth_sys/user_login_form.html"
    success_url = reverse_lazy("news_list")


class CustomUserDeleteView(DeleteView):
    model = User
    template_name = "auth_sys/user_delete_form.html"
    success_url = reverse_lazy("register")

    def get_object(self, queryset=None):
        return self.request.user


class CustomLoginMenuView(views.LoginView):
    template_name = "auth_sys/user_login_menu.html"
