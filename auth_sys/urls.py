from django.urls import path
from auth_sys import views


urlpatterns = [
    path("register/", views.user_creation, name="register"),
    path("update/", views.user_update, name="user_update"),
    path("update/password/", views.UserPasswordUpdateView.as_view(),
         name="user_password_update"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("delete/", views.CustomUserDeleteView.as_view(),
         name="delete_user"),
    path("<int:pk>/", views.user_details, name="user_details"),
]
