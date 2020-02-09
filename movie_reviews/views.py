from django.shortcuts import render
from django.contrib.auth.models import User
from movies.models import Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def user_review_page(request, user_pk):
    user = User.objects.get(pk=user_pk)
    reviews = user.moviereview_set.all()
    data = init_paginator(request.GET.get('page'), reviews)
    context = {'reviews': data, 'user': user}
    return render(request, "movie_reviews/user_reviews_list.html", context)


def movie_review_page(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    reviews = movie.moviereview_set.all()
    data = init_paginator(request.GET.get('page'), reviews)
    context = {'reviews': data, 'movie': movie}
    return render(request, "movie_reviews/movie_reviews_list.html", context)


def init_paginator(page, obj):
    paginator = Paginator(obj, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data
