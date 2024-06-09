from django.contrib import admin
from .models import Ratings

# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
    fields = ('author', 'rating', 'review', 'date',)

    ordering = ('-date',)

admin.site.register(Ratings, RatingsAdmin)