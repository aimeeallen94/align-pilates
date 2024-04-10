from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import ReservationForm
from basket.contexts import basket_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        reservation_form = ReservationForm(form_data)
        if reservation_form.is_valid():
            reservation_form.save()
            for item_id, item_data in basket.items(
                try:
                    class_type = Class_Type.objects.get(id=item_id)
            )

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Your shopping bag is empty')
            return redirect(reverse('classes'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )


    reservation_form = ReservationForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'reservation_form': reservation_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)