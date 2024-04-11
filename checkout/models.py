import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from classes.models import Class_Type
from profiles.models import UserProfile


class Reservation(models.Model):
    reservation_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, 
                                    blank=True, related_name='reservations')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    reservation_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_reservation_number(self):
        """
        Generate a random, unique reservation number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.reservation_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the reservation number
        if it hasn't been set already.
        """
        if not self.reservation_number:
            self.reservation_number = self._generate_reservation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation_number


class ReservationLineItem(models.Model):
    reservation = models.ForeignKey(Reservation, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    class_type = models.ForeignKey(Class_Type, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the reservation total.
        """
        self.lineitem_total = self.class_type.cost * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Class {self.class_type.name} on reservation: {self.reservation.reservation_number}'