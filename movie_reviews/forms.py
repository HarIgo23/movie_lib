from django import forms

from .models import MovieReview


class MovieReviewModelForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['movie', 'score', 'text',]
