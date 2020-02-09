from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
