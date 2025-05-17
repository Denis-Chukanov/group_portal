from django.shortcuts import render
from django.views.generic import ListView
from diary.models import Subject, Grade
# Create your views here.

class SubjectListView(ListView):
    model = Subject
    context_object_name = "subjects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class GradeListBySubjectView(ListView):
    model = Grade
    template_name = 'grade_list.html' 
    context_object_name = 'grades'

    def get_queryset(self):
        subject_id = self.kwargs.get('subject_id')
        return Grade.objects.filter(subject_id=subject_id)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context