from django.shortcuts import render
from django.http import HttpResponse

def calendar_popup_view(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        return HttpResponse(f"Вы выбрали дату: {selected_date}")
    return render(request, 'calendarapp/popup_calendar.html')