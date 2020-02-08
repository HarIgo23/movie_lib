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
    next_page = data.next_page_number() if data.has_next() else 1
    previous_page = data.previous_page_number() if data.has_previous() else 1
    context = {'movies': data, 'next_page': next_page, 'previous_page': previous_page}
    return render(request, "movies/movies_list.html", context)
