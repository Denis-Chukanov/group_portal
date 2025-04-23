from django.urls import path
from auth_sys import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("register/", views.user_creation, name="register"),
    path("update/", views.UserUpdateView.as_view(), name="user_update"),
    path("update/password/", views.UserPasswordUpdateView.as_view(),
         name="user_password_update"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("delete/", views.CustomUserDeleteView.as_view(),
         name="delete_user")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
