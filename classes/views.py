from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Class_Type, Level
from .forms import ClassTypeForm

# Create your views here.

def all_classes(request):
    """ A view to show the class/timetable page and all for some filtering """

    class_types = Class_Type.objects.all()
    query = None
    levels = None
    direction = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                class_types = class_types.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            class_types = class_types.order_by(sortkey)
    


    if request.GET:
        if 'level' in request.GET:
            levels = request.GET['level'].split(',')
            print(levels)
            class_types = class_types.filter(level__friendly_name__in=levels)
            print(class_types)
            levels = Level.objects.filter(friendly_name__in=levels)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "Your search didn't match any of our results")
            return redirect(reverse('classes'))

        queries = Q(name__icontains=query) | Q(teacher__icontains=query) | Q(day__icontains=query)
        class_types = class_types.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'class_types': class_types,
        'search_term': query,
        'current_levels': levels,
        'current_sorting': current_sorting,
    }

    return render(request, 'classes/classes.html', context )


def class_info(request, class_type_id):
    """ A view to show the class descriptions page """

    class_type = get_object_or_404(Class_Type, pk=class_type_id)

    context = {
        'class_type': class_type,
    }

    return render(request, 'classes/class_type.html', context )


@login_required
def add_class(request):
    """ Add a class to the timetable """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
#        class_type = get_object_or_404(Class_Type, pk=class_type_id)
        form = ClassTypeForm(request.POST, request.FILES)
#        prevent_double_bookings(class_type, class_type_id)
        if form.is_valid():
            class_type = form.save()
            messages.success(request, 'Successfully added class!')
            return redirect(reverse('class_type', args=[class_type.id]))
        else:
            messages.error(request, 'Failed to add class. Please ensure the form is valid.')
    else:
        form = ClassTypeForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_class(request, class_type_id):
    """ Edit a class_type in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    class_type = get_object_or_404(Class_Type, pk=class_type_id)
    if request.method == 'POST':
        form = ClassTypeForm(request.POST, request.FILES, instance=class_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated class!')
            return redirect(reverse('class_type', args=[class_type.id]))
        else:
            messages.error(request, 'Failed to update class type. Please ensure the form is valid.')
    else:
        form = ClassTypeForm(instance=class_type)
        messages.info(request, f'You are editing {class_type.name}')

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'class_type': class_type,
    }

    return render(request, template, context)

@login_required
def delete_class(request, class_type_id):
    """ Delete a class from the timetable """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    class_type = get_object_or_404(Class_Type, pk=class_type_id)
    class_type.delete()
    messages.success(request, 'Class deleted!')
    return redirect(reverse('classes'))