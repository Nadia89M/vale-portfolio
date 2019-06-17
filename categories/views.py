from django.shortcuts import render, get_object_or_404
from .models import Category
from photos.models import Photo

# Create your views here.
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories.html', context)

# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     subcategories = Subcategory.objects.filter(category=category)
#     return render(request, 'categories/view_category.html', {
#         'category': category,
#         'subcategories': subcategories
#     })

def view_category(request, slug):
    # category = get_object_or_404(Category, slug=slug)
    category = get_object_or_404(Category, slug=slug)
    photos = Photo.objects.filter(category=category).order_by('published_date')
    return render(request, 'categories/view_category.html', {
        'category': category,
        # 'subcategory': subcategory,
        'photos': photos
    })