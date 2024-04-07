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
    level = models.ForeignKey('Level', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    teacher = models.CharField(max_length=254)
    cost = models.DecimalField(max_digits=4, decimal_places=2)
    time = models.TimeField()
    day = models.CharField(max_length=9)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
