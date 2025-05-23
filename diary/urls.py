from django.urls import path
from diary import views


urlpatterns = [
    path("subjects", views.SubjectListView.as_view(), name="subjects"),
    path('subjects/<int:subject_id>/grades/', views.GradeListBySubjectView.as_view(), name='grades_by_subject'),
    path('subjects/create-grade<int:pk>', views.GradeCreateView, name="create-grade"),
]