from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    producer = models.CharField(max_length=256)
    duration = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']