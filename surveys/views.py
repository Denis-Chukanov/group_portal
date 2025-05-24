from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Survey, SurveyComment
from .forms import SurveyCommentForm

@login_required
def toggle_like(request, pk, comment_id):
    survey = get_object_or_404(Survey, pk=pk)
    comment = get_object_or_404(SurveyComment, pk=comment_id, survey=survey)

    # снимаем лайк со всех комментариев этого опроса
    for c in SurveyComment.objects.filter(survey=survey, liked_by=request.user):
        c.liked_by.remove(request.user)

    # добавляем/снимаем лайк на выбранном комментарии
    if request.user not in comment.liked_by.all():
        comment.liked_by.add(request.user)

    return redirect('survey_detail', pk=pk)

def survey_list(request):
    surveys = Survey.objects.filter(created_by__is_staff=True).order_by('-created_at')
    return render(request, 'survey/survey_list.html', {'surveys': surveys})

@login_required
def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    comments = (survey.comments
                .annotate(likes_count=Count('liked_by'))
                .order_by('-likes_count', '-created_at'))

    existing_comment = SurveyComment.objects.filter(survey=survey, user=request.user).first()
    can_comment = (not survey.is_closed) and (existing_comment is None)
    error = None

    if request.method == 'POST':
        if not can_comment:
            error = "Новые ответы не принимаются." if survey.is_closed else "Вы уже оставили комментарий."
        else:
            form = SurveyCommentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.survey = survey
                obj.save()
                return redirect('survey_detail', pk=pk)
    else:
        form = SurveyCommentForm()

    return render(request, 'survey/survey_detail.html', {
        'survey': survey,
        'comments': comments,
        'form': form,
        'existing_comment': existing_comment,
        'error': error,
    })