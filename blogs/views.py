from django.shortcuts import render
from .admin import Blogs
from django.contrib.auth.decorators import login_required
from blogs.forms import BlogsForm


# Create your views here.

def index(request):
    blogs = Blogs.objects
    return render(request, "blogs/home.html", {'blogs': blogs})


def detail(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


@login_required(login_url='/account/login/')
def create_blog(request):
    form = BlogsForm()
    return render(request, 'blogs/create-blog.html', {'form': form})
