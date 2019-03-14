from django.shortcuts import get_object_or_404, render
from .models import Photo

# Create your views here.

def index(request):
    photos = Photo.objects.all()
    context = {
        'photos' : photos
    }
    return render(request, 'photos/photos.html', context)

def photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = {
        'photo' : photo
    }
    return render(request, 'photos/photo.html', context)
