from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

def event_calendar(request):
    return render(request, 'calendarapp/event_calendar.html')

def event_data(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data.append({
            'title': event.title,
            'start': event.date.isoformat(),
        })
    return JsonResponse(data, safe=False)