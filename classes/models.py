from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Class_Type(models.Model):
    name = models.CharField(max_length=254)
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    description = models.TextField()
    teacher = models.CharField(max_length=254)
    cost = models.DecimalField(max_digits=4, decimal_places=2)
    time = models.TimeField()
    day = models.CharField(max_length=9)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    day_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Ratings(models.Model):
    author = models.CharField(max_length=254, null=False, blank=False)
    class_name = models.ForeignKey(Class_Type, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=False, blank=False)
    review = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)