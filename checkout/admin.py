from django.contrib import admin
from .models import Reservation, ReservationLineItem

# Register your models here.

class ReservationLineItemAdminInline(admin.TabularInline):
    model = ReservationLineItem
    readonly_fields = ('lineitem_total', 'quantity',)


class ReservationAdmin(admin.ModelAdmin):
    inlines = (ReservationLineItemAdminInline,)

    readonly_fields = ('reservation_number', 'date', 'reservation_total',)

    fields = ('reservation_number', 'full_name', 'date',
                'email', 'phone_number', 'reservation_total',)

    list_display = ('reservation_number', 'date', 'full_name',
                    'reservation_total',)

    ordering = ('-date',)

admin.site.register(Reservation, ReservationAdmin)