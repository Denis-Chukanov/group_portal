from django.urls import path
from . import views


urlpatterns = [
    path("", views.forum_main_page, name="forum_main_page"),
    path('create-thread/', views.forum_create_thread, name='forum_create_thread'),
    path('thread/<int:id>/', views.forum_thread_details, name='forum_thread_details'),
    path('thread/<int:id>/delete', views.forum_thread_delete, name='forum_confirm_delete'),
]
