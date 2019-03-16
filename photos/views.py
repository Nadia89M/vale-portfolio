from django.shortcuts import get_object_or_404, render
from categories.models import Category
from .models import Photo 

# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'photos/photos.html', context)

def photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = {
        'photo' : photo
    }
    return render(request, 'photos/photo.html', context)
