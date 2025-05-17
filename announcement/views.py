from django.shortcuts import render 
from django.views.generic import ListView , CreateView
from announcement.models import Announcement
from announcement.forms import AnnouncementForm
from django.urls import reverse_lazy
# Create your views here.

class AnnouncementView(ListView):
    model = Announcement
    context_object_name = "announcements"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AnnouncementCreate(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    success_url = reverse_lazy("announcements")
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)