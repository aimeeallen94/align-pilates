from django.contrib import admin
from .models import Reservation, ReservationLineItem


class ReservationLineItemAdminInline(admin.TabularInline):
    model = ReservationLineItem
    readonly_fields = ('lineitem_total', 'quantity',)


class ReservationAdmin(admin.ModelAdmin):
    inlines = (ReservationLineItemAdminInline,)

    readonly_fields = ('reservation_number', 'date', 'reservation_total',
                       'original_basket', 'stripe_pid',)

    fields = ('reservation_number', 'user_profile', 'full_name', 'date',
              'email', 'phone_number', 'reservation_total',
              'original_basket', 'stripe_pid',)

    list_display = ('reservation_number', 'date', 'full_name',
                    'reservation_total',)

    ordering = ('-date',)


admin.site.register(Reservation, ReservationAdmin)
