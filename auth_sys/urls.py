from django.urls import path
from auth_sys import views


urlpatterns = [
    path("register/", views.user_creation, name="register"),
    path("update/", views.user_update, name="user_update"),
    path("update/password/", views.UserPasswordUpdateView.as_view(),
         name="user_password_update"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("delete/", views.CustomUserDeleteView.as_view(),
         name="user_delete"),
    path("<int:pk>/", views.user_details, name="user_details"),
    path("logout/", views.logout_view, name="logout"),
    path("login-menu/", views.CustomLoginMenuView.as_view(), name="user_login_menu"),
    path("", views.request_user_details, name="request_user_details"),
]
