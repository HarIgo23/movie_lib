from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer


def movies_list_view(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'movies': data}
    return render(request, "movies/movies_list.html", context)


class MovieView(APIView):
    """
    Get movies list and create movie
    """
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})

    def post(self, request):
        movie = request.data.get('movie')

        serializer = MovieSerializer(data=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    """
    Get movie, update movie and delete movie
    """
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response({'movie': serializer.data})

    def put(self, request, pk):
        saved_movie = get_object_or_404(Movie.objects.all(), pk=pk)
        movie = request.data.get('movie')
        serializer = MovieSerializer(instance=saved_movie, data=movie, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie.objects.all(), pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
