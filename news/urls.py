from django.urls import path
from news import views


urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("projects/", views.ProjectList.as_view(), name="project_list"),
    path("projects/<int:pk>/", views.ProjectDetails.as_view(),
         name="project_details"),
]
