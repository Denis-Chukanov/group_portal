from django.urls import path
from announcement import views


urlpatterns = [
    path("", views.AnnouncementView.as_view(), name="announcements")
]