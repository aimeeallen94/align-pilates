from django.contrib import admin
from .models import Level, Class_Type, Ratings

# Register your models here.


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class Class_TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'teacher',
        'day',
        'time',
        'cost',
        'day_number',
    )


class RatingsAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    
    fields = ('author', 'class_name', 'rating', 'review', 'date',)

    ordering = ('-date',)


admin.site.register(Ratings, RatingsAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Class_Type, Class_TypeAdmin)
