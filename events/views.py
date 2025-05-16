from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.order_by('date')
    return render(request, 'events/event_list.html', {'events': events})
