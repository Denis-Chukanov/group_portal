from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.event_calendar, name='event_calendar'),
    path('calendar/data/', views.event_data, name='event_data'),
]