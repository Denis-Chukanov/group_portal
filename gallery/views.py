from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from auth_sys.decorators import is_moderator, is_administrator
from .models import Image
from .forms import ImageUploadForm



def validate_images(request, pk):
    images = Image.objects.filter(is_approved=False, created_by=pk).order_by('-created_at')

    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        action = request.POST.get('action')
        image = get_object_or_404(Image, id=image_id)

        if action == 'approve':
            image.is_approved = True
            image.save()
            messages.success(request, f"Изображение '{image.title}' одобрено.")
        elif action == 'delete':
            image.delete()
            messages.success(request, f"Изображение '{image.title}' удалено.")
        return redirect('validate_images')

    return render(request, 'gallery/gallery_validate_images.html', {'images': images})


def gallery(request):
    user = request.user
    
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.created_by = user
            image.save()
            return redirect('gallery')
    else:
        form = ImageUploadForm()
        
    if request.user == user:
        images = Image.objects.filter(created_by=user).order_by('-created_at')
    else:
        images = Image.objects.filter(created_by=user, is_approved=True).order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'images': images, 'form': form})


def user_gallery(request, username):
    user = get_object_or_404(User, username=username)

    is_staff = request.user == user or request.user.groups.filter(name__in=['moderator', 'administrator']).exists()

    if is_staff:
        images = Image.objects.filter(created_by=user).order_by('-created_at')
    else:
        images = Image.objects.filter(created_by=user, is_approved=True).order_by('-created_at')

    return render(request, 'gallery/user_gallery.html', {
        'images': images,
        'viewed_user': user
    })