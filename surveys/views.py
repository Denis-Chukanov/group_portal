from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, SurveyComment
from django.contrib.auth.decorators import login_required
from .forms import SurveyCommentForm

def survey_list(request):
    surveys = Survey.objects.filter(created_by__is_staff=True).order_by('-created_at')
    return render(request, 'survey/survey_list.html', {'surveys': surveys})

@login_required
def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    comments = survey.comments.all()

    if request.method == 'POST':
        form = SurveyCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.survey = survey
            comment.save()
            return redirect('survey_detail', pk=survey.pk)
    else:
        form = SurveyCommentForm()

    return render(request, 'survey/survey_detail.html', {
        'survey': survey,
        'comments': comments,
        'form': form
    })
