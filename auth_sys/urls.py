from django.urls import path
from auth_sys import views


urlpatterns = [
    path("register/", views.UserCreationView.as_view(), name="register"),
    path("update/", views.UserUpdateView.as_view(), name="user_update"),
    path("update/password/", views.UserPasswordUpdateView.as_view(),
         name="user_password_update"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("delete/", views.CustomUserDeleteView.as_view(),
         name="delete_user")
]
