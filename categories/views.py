from django.shortcuts import render, get_object_or_404
from .models import Category
from photos.models import Photo

# Create your views here.
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    photos = Photo.objects.filter(category=category)
    return render(request, 'categories/view_category.html', {
        'category': category,
        'photos': photos
    })