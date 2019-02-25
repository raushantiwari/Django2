from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .admin import Blogs
from django.contrib.auth.decorators import login_required
from blogs.forms import BlogsForm
import datetime


# Create your views here.

def index(request):
    blogs = Blogs.objects.all()
    paginator = Paginator(blogs, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    blog = paginator.get_page(page)
    return render(request, "blogs/home.html", {'blogs': blog})


def detail(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


@login_required(login_url='/account/login/')
def create_blog(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['image'] and request.POST['body']:
            blog = Blogs()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            blog.author = request.user
            blog.pub_date = datetime.datetime.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogsForm()
        return render(request, 'blogs/create-blog.html', {'form': form})


@login_required(login_url='/account/login/')
def edit_blog(request, blogid):
    if request.method == 'POST':
        blog = Blogs()
        blog.title = request.POST['title']
        blog.pub_date = datetime.datetime.now()
        blog.image = request.FILES['image']
        blog.save()
        return redirect('/blog/' + str(blog.id))
    else:
        blog = Blogs.objects.get(id=blogid)
        return render(request, 'blogs/edit-blog.html', {'blog': blog})
