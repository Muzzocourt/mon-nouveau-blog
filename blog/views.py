from django.shortcuts import render
# pour importer le modele situé dans models.py
from .models import Post
# pour importer les fichiers par date 
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})