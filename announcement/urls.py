from django.urls import path
from announcement import views


urlpatterns = [
    path("announcements", views.AnnouncementView.as_view(), name="announcements")
]