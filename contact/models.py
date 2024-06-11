from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class ContactDetails(models.Model):
    """
    Contact details model for contact us form
    """
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    query = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=20, null=False, blank=False)


@receiver(post_save, sender=ContactDetails)
def send_contact_form(sender, instance, created, **kwargs):
    instance.contact_details.post_save(instance.full_name, instance.email, instance.query, instance.phone_number)
