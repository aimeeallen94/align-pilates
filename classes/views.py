from django.shortcuts import render
from .models import Class_Type

# Create your views here.

def all_classes(request):
    """ A view to show the class/timetable page and all for some filtering """

    class_types = Class_Type.objects.all

    context = {
        'class_types': class_types,
    }

    return render(request, 'classes/classes.html', context )
