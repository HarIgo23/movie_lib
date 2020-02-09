from django.urls import path

from .views import (
    MovieView,
    MovieDetailView,
)


app_name = "movies"


urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:pk>', MovieDetailView.as_view())
]
