from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from auth_sys.decorators import is_moderator, is_administrator
from .models import Image
from django.contrib.auth.models import User
from .forms import ImageUploadForm

@login_required
def gallery(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.created_by = request.user
            image.save()
            return redirect('gallery')
    else:
        form = ImageUploadForm()

    images = Image.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'images': images, 'form': form})

def user_gallery(request, username):
    user = get_object_or_404(User, username=username)
    images = Image.objects.filter(created_by=user).order_by('-created_at')
    return render(request, 'gallery/user_gallery.html', {
        'images': images,
        'viewed_user': user
    })