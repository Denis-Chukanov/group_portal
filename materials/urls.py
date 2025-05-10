from django.urls import path
from materials import views


urlpatterns = [
    path("investment/<int:pk>/", views.investment_details,
         name="investment_details"),
    path("subjects/", views.SubjectList.as_view(),
         name="subject_list"),
    path("subject/<int:pk>/", views.MaterialList.as_view(),
         name="material_list"),
    path("<int:pk>/", views.MaterialDetailView.as_view(),
         name="material_details"),
]
