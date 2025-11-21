from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from .forms import MediaForm

def media_list(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaForm()
    
    media = Media.objects.all()
    return render(request, 'media_app/media_list.html', {'media': media, 'form': form})

def delete_media(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    media.delete()
    return redirect('media_list')

def edit_media(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaForm(instance=media)
    
    return render(request, 'media_app/edit_media.html', {'form': form, 'media': media})
