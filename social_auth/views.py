from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login_page(request):
    return render(request, 'social_auth/login.html')


@login_required
def profile_page(request):
    return render(request, 'social_auth/profile.html')
