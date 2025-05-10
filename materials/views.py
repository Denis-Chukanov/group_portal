from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from auth_sys.mixins import UserIsStudentMixin
from materials import models
from django.contrib.auth.decorators import login_required
from auth_sys.decorators import is_student


# Create your views here.
@login_required
@is_student
def investment_details(request, pk):
    investment = models.Investment.objects.get(pk=pk)
    if investment.media:
        return redirect(investment.media.url)

    else:
        return redirect(investment.adress)


class SubjectList(LoginRequiredMixin, UserIsStudentMixin, ListView):
    model = models.Subject
    template_name = "materials/subject_list.html"
    context_object_name = "subjects"


class MaterialList(LoginRequiredMixin, UserIsStudentMixin, ListView):
    model = models.Material
    template_name = "materials/material_list.html"
    context_object_name = "materials"

    def get_queryset(self):
        queryset = super().get_queryset()
        subject_id = self.kwargs.get("pk")
        subject = models.Subject.objects.get(pk=subject_id)
        queryset = queryset.filter(subject=subject)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs.get("pk")
        subject = models.Subject.objects.get(pk=subject_id)
        context["subject"] = subject

        return context


class MaterialDetailView(LoginRequiredMixin, UserIsStudentMixin, DetailView):
    model = models.Material
    template_name = "materials/material_details.html"
    context_object_name = "material"
