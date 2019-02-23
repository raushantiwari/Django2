from django.shortcuts import render
from .admin import Blogs


# Create your views here.

def index(request):
    blogs = Blogs.objects
    return render(request, "blogs/home.html", {'blogs': blogs})


def top_five(request):
    return render(request, 'blogs/top5.html')


def detail(request, blog_id):
    blog = Blogs.objects.get(id = blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
