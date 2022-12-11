from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_redirect')
        else:
            messages.success(request, ("Please enter valid login information!"))
            return redirect('login')
    else:
        return render(request, 'customer_page.html', {})

def login_redirect(request):
    user = request.user
    if user.is_superuser:
        return redirect('home')
    else:
        return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('login')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"