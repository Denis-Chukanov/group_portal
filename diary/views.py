from django.shortcuts import render, redirect
from django.views.generic import ListView , CreateView
from diary.models import Subject, Grade
from diary.forms import GradeForm
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
        context['form'] = GradeForm()
        context['subject_id'] = self.kwargs.get('subject_id')  
        return context
    
def GradeCreateView(request, pk):
    subject_id = pk
    if request.method == "POST":
        grade_form = GradeForm(request.POST)
        if grade_form.is_valid():
            grade = grade_form.save(commit=False)
            grade.subject_id = subject_id
            grade.save()
            return redirect("grades_by_subject", subject_id=subject_id)
    else:
        grade_form = GradeForm()
        