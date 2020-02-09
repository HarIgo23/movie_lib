from django.urls import path

from .views import (
    MovieReviewView,
    MovieReviewDetailView,
    movie_review_api,
    user_review_api
)


app_name = "movies_review"


urlpatterns = [
    path('reviews/', MovieReviewView.as_view()),
    path('reviews/<int:pk>', MovieReviewDetailView.as_view()),
    path('reviews/user/<int:pk>', user_review_api),
    path('reviews/movie/<int:pk>', movie_review_api),
]
