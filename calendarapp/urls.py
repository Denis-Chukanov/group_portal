from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_popup_view, name='calendar'),  # или другой view
]