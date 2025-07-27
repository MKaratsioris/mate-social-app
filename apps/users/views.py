from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.users.forms import MateRegisterForm

def index(request):
    return render(request, 'users/index.html')

@login_required
def home(request):
    return render(request, 'users/home.html')

def signin(request):
    if request.method=="POST":
        register_form = MateRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user account created successfully! Login to get started!"))
            return redirect('login')
    register_form = MateRegisterForm()
    return render(request, 'users/signin.html', {'register_form': register_form})