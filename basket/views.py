from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from classes.models import Class_Type


def view_basket(request):
    """ A view to return the shopping basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, class_id):
    """ A view to return the shopping basket page """

    class_chosen = get_object_or_404(Class_Type, pk=class_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if class_id in list(basket.keys()):
        basket[class_id] += quantity
    else:
        basket[class_id] = quantity
        messages.success(request, f'Added {class_chosen.name} to your bag.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """ A view to remove items from bag """

    class_chosen = get_object_or_404(Class_Type, pk=item_id)

    try:
        basket = request.session.get('basket', {})
        basket.pop(str(item_id))
        messages.success(request, f'Removed {class_chosen.name} \
        from your bag.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e} from your bag.')
        return HttpResponse(status=500)
