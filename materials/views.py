from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from auth_sys.mixins import UserIsStudentMixin
from materials import models


# Create your views here.
class InvestmentDetails(LoginRequiredMixin, UserIsStudentMixin, DetailView):
    template_name = "materials/investment_details.html"
    context_object_name = "investerment"
    model = models.Investment


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
