from django.contrib import admin
from .models import Level, Class_Type

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
        'rating',
        'cost',
        'day_number',
    )

admin.site.register(Level, LevelAdmin)
admin.site.register(Class_Type, Class_TypeAdmin)