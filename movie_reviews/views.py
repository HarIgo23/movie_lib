from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view

from movies.models import Movie
from .models import MovieReview
from django.contrib.auth.models import User
from .serializers import MovieReviewSerializer


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


class MovieReviewView(APIView):
    """
    Get movies reviews list and create movie review
    """
    def get(self, request):
        movies_reviews = MovieReview.objects.all()
        serializer = MovieReviewSerializer(movies_reviews, many=True)
        return Response({'movies_reviews': serializer.data})

    def post(self, request):
        movie_review = request.data.get('movie_review')

        serializer = MovieReviewSerializer(data=movie_review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieReviewDetailView(APIView):
    """
    Get movie review, update movie review and delete movie review
    """
    def get(self, request, pk):
        movie_review = MovieReview.objects.get(pk=pk)
        serializer = MovieReviewSerializer(movie_review)
        return Response({'movie_review': serializer.data})

    def put(self, request, pk):
        saved_movie = get_object_or_404(MovieReview.objects.all(), pk=pk)
        movie_review = request.data.get('movie_review')
        serializer = MovieReviewSerializer(instance=saved_movie, data=movie_review, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie_review = get_object_or_404(MovieReview.objects.all(), pk=pk)
        movie_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_review_api(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    reviews = user.moviereview_set.all()
    serializer = MovieReviewSerializer(reviews, many=True)
    return Response({'movies_reviews': serializer.data})


@api_view(['GET'])
def movie_review_api(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    reviews = movie.moviereview_set.all()
    serializer = MovieReviewSerializer(reviews, many=True)
    return Response({'movies_reviews': serializer.data})

def delete_review_page(request, pk):
    movie_review = get_object_or_404(MovieReview.objects.all(), pk=pk)
    movie_review.delete()
    return redirect('profile')