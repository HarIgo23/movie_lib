from rest_framework import serializers
from .models import MovieReview


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ['id', 'user', 'movie', 'score', 'text', 'date_create', 'date_update']
