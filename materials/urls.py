from django.urls import path
from materials import views


urlpatterns = [
    path("investment/<int:pk>/", views.InvestmentDetails.as_view(),
         name="investment_details"),
    path("subjects/", views.SubjectList.as_view(),
         name="subject_list")
]
