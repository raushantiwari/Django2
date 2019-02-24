from django.shortcuts import render, redirect
from .admin import Blogs
from django.contrib.auth.decorators import login_required
from blogs.forms import BlogsForm
import datetime

# Create your views here.

def index(request):
    blogs = Blogs.objects
    return render(request, "blogs/home.html", {'blogs': blogs})


def detail(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


@login_required(login_url='/account/login/')
def create_blog(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['author'] and request.FILES['image'] and request.POST['body']:
            blog = Blogs()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            # blog.published = request.POST['published']
            blog.author = request.POST['author']
            blog.pub_date = datetime.datetime.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogsForm()
    return render(request, 'blogs/create-blog.html', {'form': form})
