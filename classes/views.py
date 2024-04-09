from django.shortcuts import render, get_object_or_404
from .models import Class_Type

# Create your views here.

def all_classes(request):
    """ A view to show the class/timetable page and all for some filtering """

    class_types = Class_Type.objects.all

    context = {
        'class_types': class_types,
    }

    return render(request, 'classes/classes.html', context )


def class_info(request, class_type_id):
    """ A view to show the class descriptions page """

    class_type = get_object_or_404(Class_Type, pk=class_type_id)

    context = {
        'class_type': class_type,
    }

    return render(request, 'classes/class_type.html', context )