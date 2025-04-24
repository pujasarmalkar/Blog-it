from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout
from django.conf import settings

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from blog.models import Blog

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            return redirect('home')
        else:

            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form, 'errors': form.errors})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)

def home_view(request):
    if request.user.is_authenticated:
        return redirect('user')  
    return render(request, 'home.html')


def user_view(request):

    user_blogs = Blog.objects.filter(author=request.user)
    
    context = {
        'user': request.user,
        'user_blogs': user_blogs,
    }
    
    return render(request, 'user.html', context)
