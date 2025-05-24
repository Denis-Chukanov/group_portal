from django.urls import path
from diary import views


urlpatterns = [
    path("subjects", views.SubjectListView.as_view(), name="subjects"),
    path('subjects/<int:subject_id>/grades/', views.GradeListBySubjectView.as_view(), name='grades_by_subject'),
    path('subjects/create-grade<int:pk>', views.GradeCreateView, name="create-grade"),
    path('subjects/create-subject', views.SubjectCreateView.as_view(), name="create-subject"),
    path('grades/<int:pk>/delete/', views.GradeDeleteView.as_view(), name="delete-grade"),
    path('grades/update-grade<int:pk>', views.GradeUpdateView.as_view(), name="update-grade")
]