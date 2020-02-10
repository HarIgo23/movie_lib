"""MovieList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import (
    home_page,
    api_page,
)
from movies.views import (
    movies_list_view
)
from movie_reviews.views import (
    movie_review_page,
    user_review_page,
)
from social_auth.views import (
    login_page,
    profile_page,
    register_page,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('movie/', movies_list_view, name='movie-list'),
    url(r'^movie/(?P<movie_pk>[0-9]+)$', movie_review_page, name='movie-review'),
    url(r'^user/(?P<user_pk>[0-9]+)$', user_review_page, name='user-review'),
    path('api/', api_page, name='api-list'),
    path('api/', include('movies.urls')),
    path('api/', include('movie_reviews.urls')),
    path('login/', LoginView.as_view(template_name="social_auth/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile', profile_page, name='profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('register/', register_page, name='register')
]
