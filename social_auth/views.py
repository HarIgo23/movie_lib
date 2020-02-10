from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_page(request):
    return render(request, 'social_auth/login.html')


@login_required
def profile_page(request):
    return render(request, 'social_auth/profile.html')


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect('profile')
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "social_auth/register.html", context)