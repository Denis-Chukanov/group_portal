from django.shortcuts import render
from .models import News, Project
from django.views.generic import ListView, DeleteView
from django.contrib.auth.models import User


def news_list(request):
    news = News.objects.all().order_by('-published_at')
    return render(request, 'news/news_list.html', {'news': news})


class ProjectList(ListView):
    model = Project
    template_name = "news/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.GET.get("user-id")
        if user_id:
            user = User.objects.get(pk=user_id)
            queryset = queryset.filter(author=user)
        return queryset


class ProjectDetails(DeleteView):
    model = Project
    template_name = "news/project_details.html"
    context_object_name = "project"
