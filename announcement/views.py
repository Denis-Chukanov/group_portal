from django.shortcuts import render
from django.views.generic import ListView
from announcement.models import Announcement
# Create your views here.

class AnnouncementView(ListView):
    model = Announcement
    context_object_name = "announcements"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
