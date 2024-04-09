from django.shortcuts import render, redirect

# Create your views here.

def view_basket(request):
    """ A view to return the shopping basket page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, class_id):
    """ A view to return the shopping basket page """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if class_id in list(basket.keys()):
        basket[class_id] += quantity
    else:
        basket[class_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)