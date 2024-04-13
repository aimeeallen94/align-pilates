from django.db import models

class ContactDetails(models.Model):
    """
    Contact details model for contact us form
    """
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    query = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=20, null=False, blank=False)