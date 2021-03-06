from django.db import models
from django.conf import settings
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator

User = settings.AUTH_USER_MODEL


class UserMovieReviewManager(models.Manager):
    def user_review(self, user):
        return super().get_queryset().filter(user=user)

class MovieReview(models.Model):
    # relationship "backward"
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#backwards-related-objects
    # user have moviereview_set for query
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    text = models.TextField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-score']
