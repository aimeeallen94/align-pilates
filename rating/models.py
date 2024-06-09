from django.db import models

from classes.models import Class_Type

# Create your models here.

class Ratings(models.Model):
    author = models.CharField(max_length=254, null=False, blank=False)
    class_name = models.ForeignKey(Class_Type, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=2, null=False, blank=False)
    review = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
        