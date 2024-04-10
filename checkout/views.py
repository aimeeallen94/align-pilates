from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import ReservationForm
from .models import Reservation, ReservationLineItem
from classes.models import Class_Type
from basket.contexts import basket_contents

import stripe
import json 

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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
            reservation = reservation_form.save()
            for item_id, item_data in basket.items():
                try:
                    class_type = Class_Type.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        reservation_line_item = ReservationLineItem(
                            reservation=reservation,
                            class_type=class_type,
                            quantity=item_data,
                        )
                        reservation_line_item.save()
                except Class_Type.DoesNotExist:
                    messages.error(request, ('One of the classes you have tried to book seems to be displaying an error. \
                        Please call us for assistance.')
                        )
                    reservation.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[reservation.reservation_number]))
        else:
            messages.error(request, 'There was an error with your booking. Please double check all details provided.')
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

def checkout_success(request, reservation_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    messages.success(request, f'Reservation successfully processed! \
        Your reservation number is {reservation_number}. A confirmation \
        email will be sent to {reservation.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'reservation': reservation,
    }

    return render(request, template, context)