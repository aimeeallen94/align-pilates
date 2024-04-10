from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ReservationLineItem

@receiver(post_save, sender=ReservationLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ 
    Update reservation as lineitems added 
    """
    instance.reservation.update_total()


@receiver(post_delete, sender=ReservationLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update reservation as line items deleted
    """
    instance.reservation.update_total()