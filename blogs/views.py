from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "blogs/home.html")


def top_five(request):
    return render(request, 'blogs/top5.html')
