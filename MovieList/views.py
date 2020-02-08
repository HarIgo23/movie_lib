from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_page(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    next_page = data.next_page_number() if data.has_next() else 1
    previous_page = data.previous_page_number() if data.has_previous() else 1
    context = {'users': data, 'next_page': next_page, 'previous_page': previous_page}
    return render(request, "home.html", context)
