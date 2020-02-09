from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_page(request):
    users = User.objects.all().order_by('username')
    paginator = Paginator(users, 10)

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'users': data}
    return render(request, "home.html", context)


def api_page(request):
    return render(request, 'api.html')
