from django.urls import path
from . import views


urlpatterns = [
    path("", views.forum_main_page, name="forum_main_page"),
    path('create-thread/', views.ThreadCreationView.as_view(), name='forum_creation_thread'),
    path('thread/<int:id>/', views.forum_thread_details, name='forum_thread_details'),
    path('thread/<int:id>/delete', views.forum_thread_delete, name='forum_confirm_delete'),
    path("f/", views.forum_redirect, name='forum_redirect'),
]
