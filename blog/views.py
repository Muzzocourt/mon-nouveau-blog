from django.shortcuts import render, get_object_or_404
# pour importer le modele situé dans models.py
from .models import Post
# pour importer les fichiers par date 
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# vue pour le détail de chaque post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})