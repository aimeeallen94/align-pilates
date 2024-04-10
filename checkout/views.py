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
        'stripe_public_key': 'pk_test_51P41YxKxh0iNjxuCiVPsxJ4jfhxyjqfokMyglR9KQ8ZMu01EqrQAkqNUlMPk4PZ1Ef0kTsRqvK06HwfnLZPFIJWu00hWm7ZmMr',
        'client_secret': 'client secret key',
    }

    return render(request, template, context)