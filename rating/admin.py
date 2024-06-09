from django.contrib import admin
from .models import Ratings

# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    
    fields = ('author', 'class_name', 'rating', 'review', 'date',)

    ordering = ('-date',)

admin.site.register(Ratings, RatingsAdmin)