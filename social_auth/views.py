from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from movie_reviews.forms import MovieReviewModelForm
from movie_reviews.models import MovieReview


def login_page(request):
    return render(request, 'social_auth/login.html')


@login_required
def profile_page(request):
    form = MovieReviewModelForm(request.POST or None)
    user = request.user
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        form = MovieReviewModelForm()
        messages.success(request, "Review added successful")
    reviews = user.moviereview_set.all()
    context = {'form_review': form, 'reviews': reviews}
    return render(request, 'social_auth/profile.html', context)


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