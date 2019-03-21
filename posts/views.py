from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/posts.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post
    }
    return render(request, 'blog/post.html', context)
