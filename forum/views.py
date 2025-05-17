from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from auth_sys.decorators import is_moderator, is_administrator
from django.urls import reverse_lazy
import markdown
from .models import Thread
from .forms import PostForm, ThreadForm


def forum_main_page(request):
    threads = Thread.objects.all().order_by('created_at')
    return render(request, 'forum/forum_main_page.html', {'threads': threads})

def forum_redirect(request):
    return render(request, 'forum/forum_redirect.html')

@login_required
def forum_create_thread(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        attachment = request.POST.get('attachment')
        if title:
            Thread.objects.create(title=title, content=content, attachment=attachment, created_by=request.user)
            return redirect('forum_main_page')
        else:
            return HttpResponse("Title is required for post.")
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
    
@login_required
def forum_thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id, created_by=request.user)
    
    
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('forum_thread_details', id=thread.id)
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'forum/forum_edit.html', {'form': form, 'thread': thread})
    
    
@login_required
def forum_thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    
    if (request.user != thread.created_by or not is_moderator(request.user) or not is_administrator(request.user)):
        return HttpResponse("You cannot delete this thread.")
    
    if request.method == 'POST':
        thread.delete()
        return redirect('forum_main_page')
    
    return render(request, 'forum/forum_confirm_delete.html', {'thread': thread})

class ThreadCreationView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "forum/forum_creation_thread.html"
    success_url = reverse_lazy("forum_main_page")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)
    

