from django.shortcuts import redirect
from django.views.generic import ListView , CreateView , DeleteView , UpdateView
from diary.models import Subject, Grade
from diary.forms import GradeForm, SubjectForm
from django.urls import reverse_lazy , reverse
# Create your views here.

class SubjectListView(ListView):
    model = Subject
    context_object_name = "subjects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SubjectForm
        return context
    
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy("subjects")
    def form_valid(self, form):
        form.instance.creator = self.request.user 
        return super().form_valid(form)

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
    
class GradeDeleteView(DeleteView):
    model = Grade
    def get_success_url(self):
        subject_id = self.object.subject_id 
        return reverse("grades_by_subject", kwargs={"subject_id": subject_id})

class GradeUpdateView(UpdateView):
    model = Grade
    fields = ['grade']

    def get_success_url(self):
        return reverse_lazy('grades_by_subject', kwargs={'subject_id': self.object.subject_id})


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
        
