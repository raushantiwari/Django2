from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['name'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('blog_home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and Password is Invalid.'})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confpass']:
            try:
                user = User.objects.get(username=request.POST['name'])
                return render(request, 'accounts/signup.html', {'error': 'Username already taken.'})
            except User.DoesNotExist:
                try:
                    email = User.objects.get(email=request.POST['email'])
                    return render(request, 'accounts/signup.html', {'error': 'Email already taken.'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['name'], password=request.POST['pass'],
                                                    email=request.POST['email'])
                    auth.login(request, user)
                    return redirect('blog_home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password doest not match.'})
    else:
        return render(request, 'accounts/signup.html')


def forgot_pass(request):
    return render(request, 'accounts/forgot.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog_home')
