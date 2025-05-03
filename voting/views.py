from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Poll, Vote
from .forms import VoteForm

def poll_list(request):
    polls = Poll.objects.all().order_by('-created_at')
    return render(request, 'voting/poll_list.html', {'polls': polls})

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    try:
        vote = Vote.objects.get(user=request.user, poll=poll)
    except Vote.DoesNotExist:
        vote = None

    if request.method == 'POST':
        form = VoteForm(poll, request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            Vote.objects.update_or_create(
                user=request.user,
                poll=poll,
                defaults={'choice': choice}
            )
            return redirect('voting:poll_list')
    else:
        form = VoteForm(poll)

    return render(request, 'voting/poll_detail.html', {
        'poll': poll,
        'form': form,
        'previous_vote': vote
    })