from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
# The logic of your application goes here; each view receives an HTTP request, pro-
# cesses it, and returns a response.
# Create your views here.

def post_list(request):
    post = Post.published.all()
    return render(request,'blog/post/list.html', {'post':post})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status = Post.Status.PUBLISHED)
        
    return render(request,'blog/post/detail.html', {'post': post})

 
