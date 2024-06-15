from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Reservation, ReservationLineItem
from classes.models import Class_Type
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, reservation):
        """Send the user a confirmation email"""
        cust_email = reservation.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'reservation': reservation})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'reservation': reservation,
                'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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
        try:
            intent = event.data.object
            pid = intent.id
            basket = intent.metadata.basket
            save_info = intent.metadata.save_info

            # Get the Charge object
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )

            billing_details = stripe_charge.billing_details
            reservation_total = round(stripe_charge.amount / 100, 2)

            # Update profile information if save_info was checked
            profile = None
            username = intent.metadata.username
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = billing_details.phone
                    profile.email = billing_details.email
                    profile.save()

            reservation_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    reservation = Reservation.objects.get(
                        full_name__iexact=billing_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=billing_details.phone,
                        reservation_total=reservation_total,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    reservation_exists = True
                    break
                except Reservation.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
            if reservation_exists:
                self._send_confirmation_email(reservation)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | \
                    SUCCESS: Verified reservation already in database',
                    status=200)
            else:
                reservation = None
                try:
                    reservation = Reservation.objects.create(
                        full_name=billing_details.name,
                        user_profile=profile,
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
                    print('exception -couldnt create reservation sebd 500 error')
                    if reservation:
                        reservation.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
            self._send_confirmation_email(reservation)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                        SUCCESS: Created reservation in webhook',
                status=200)
        except Exception as error:
            print(error)
            print(type(error).__name__)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
