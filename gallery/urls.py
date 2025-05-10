from django.urls import path
from . import views


urlpatterns = [
    path("", views.gallery, name="gallery"),
    path('gallery/<str:username>/', views.user_gallery, name='user_gallery'),
]