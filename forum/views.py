from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Thread, Post
from .forms import PostForm


def forum_main_page(request):
    threads = Thread.objects.all().order_by('created_at')
    return render(request, 'forum/forum_main_page.html', {'threads': threads})


@login_required
def forum_create_thread(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title:
            Thread.objects.create(title=title, content=content, created_by=request.user)
            return redirect('forum_main_page')
        else:
            return HttpResponse("Title is required.")
    return redirect('forum_main_page')


@login_required
def forum_thread_details(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.select_related('created_by').all()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('forum_thread_details', id=thread.id)
    else:
        form = PostForm()

    return render(request, 'forum/forum_details.html', {
        'thread': thread,
        'all_posts': posts,
        'form': form,
    })