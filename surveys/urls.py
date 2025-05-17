from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_list, name='survey_list'),
    path('<int:pk>/', views.survey_detail, name='survey_detail'),
    path('<int:pk>/like/<int:comment_id>/', views.toggle_like, name='toggle_like'),
]