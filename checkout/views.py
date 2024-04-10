from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ReservationForm

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your shopping bag is empty')
        return redirect(reverse('classes'))

    reservation_form = ReservationForm()
    template = 'checkout/checkout.html'
    context = {
        'reservation_form': reservation_form,
    }

    return render(request, template, context)