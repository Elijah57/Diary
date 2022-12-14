from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def  register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("login-site")

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", context={"form": form})

@login_required(login_url="login-site")
def profile(request):
    return render(request, "users/profile.html")
    
