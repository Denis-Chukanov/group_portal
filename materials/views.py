from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from auth_sys.mixins import UserIsStudentMixin, UserIsModeratorMixin
from materials import models
from django.contrib.auth.decorators import login_required
from auth_sys.decorators import is_student
from materials import forms
from django.core.paginator import Paginator
from materials.decorators import is_comment_owner
from materials.mixins import UserIsSubjectOwnerMixin


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


@login_required
@is_student
def material_details(request, pk):
    material = models.Material.objects.get(pk=pk)
    comments = models.Comment.objects.filter(material=material)
    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.material = material
            comment.save()
        return redirect("material_details", pk=comment.material.pk)

    paginator = Paginator(comments, 8)
    page_number = request.GET.get("page")
    page_comments = paginator.get_page(page_number)
    context = {
        "material": material,
        "comment_form": forms.CommentForm,
        "comments": page_comments,
    }

    return render(request,
                  "materials/material_details.html",
                  context)


@login_required
@is_comment_owner
def comment_update(request, pk):
    comment = models.Comment.objects.get(pk=pk)
    material_pk = comment.material.pk
    material = models.Material.objects.get(pk=material_pk)
    comments = models.Comment.objects.filter(material=material)
    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            return redirect("material_details", pk=comment.material.pk)

    paginator = Paginator(comments, 8)
    page_number = request.GET.get("page")
    page_comments = paginator.get_page(page_number)
    context = {
        "material": material,
        "comment_form": forms.CommentForm(instance=comment),
        "comments": page_comments,
    }

    return render(request,
                  "materials/material_details.html",
                  context)


@login_required
@is_comment_owner
def comment_delete(request, pk):
    comment = models.Comment.objects.get(pk=pk)
    material_pk = comment.material.pk
    comment.delete()
    return redirect("material_details", pk=material_pk)


class SubjectUpdateForm(LoginRequiredMixin, UserIsSubjectOwnerMixin,
                        UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    template_name = "materials/subject_update_form.html"
    success_url = reverse_lazy("news_list")


class SubjectCreateForm(LoginRequiredMixin, UserIsModeratorMixin,
                        CreateView):
    model = models.Subject
    form_class = forms.SubjectForm
    template_name = "materials/subject_create_form.html"
    success_url = reverse_lazy("news_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def material_create(request):
    if request.method == "POST":
        material_form = forms.MaterialForm(request.POST)
        media = request.POST.get("media")
        adress = request.POST.get("adress")
        material = material_form.save(commit=False)
        request.session["investments"] = []
        print(media)
        if media != "":
            media_object = models.Investment(media=media,
                                             material=material)
            request.session["investments"].append(media_object)
        elif adress is not None:
            adress_object = models.Investment(adress=adress,
                                              material=material)
            request.session["investments"].append(adress_object)
        if material_form.is_valid():
            material = material_form.save()
            for investment in request.session["investments"]:
                investment.save()
            del request.session["investments"]
            return redirect("material_details", pk=material.pk)
        return redirect("material_create")

    context = {
        "material_form": forms.MaterialForm,
    }
    return render(
        request,
        "materials/material_create_form.html",
        context
    )
