from django.contrib import admin
from .models import ContactDetails

# Register your models here.

class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'query',
        'phone_number',
    )


admin.site.register(ContactDetails, ContactDetailsAdmin)