from django.http import HttpResponse

from .models import Reservation, ReservationLineItem
from classes.models import Class_Type

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
        intent.latest_charge
        )

        billing_details = stripe_charge.billing_details 
        grand_total = round(intent.charges.data[0].amount / 100, 2)
       
        reservation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                reservation__iexact= Reservation.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                reservation_exists = True
                break
            except Reservation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if reservation_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified reservation already in database',
                status=200)
        else:
            reservation = None
            try:
                reservation = Reservation.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    class_type = Class_Type.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        reservation_line_item = ReservationLineItem(
                            reservation=reservation,
                            class_type=class_type,
                            quantity=item_data,
                        )
                        reservation_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            reservation_line_item = ReservationLineItem(
                                reservation=reservation,
                                class_type=class_type,
                                quantity=quantity,
                            )
                            reservation_line_item.save()
            except Exception as e:
                if reservation:
                    reservation.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created reservation in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)