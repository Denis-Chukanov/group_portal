from django.urls import path
from . import views


urlpatterns = [
    path("forum/", views.forum_main_page, name="forum_main_page"),
    path('create-thread/', views.forum_create_thread, name='forum_create_thread'),
    path('thread/<int:id>/', views.forum_thread_details, name='thread_details'),
]
