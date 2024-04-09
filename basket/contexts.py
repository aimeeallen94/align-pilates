from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from classes.models import Class_Type

def basket_contents(request):

    basket_items = []
    grand_total = 0
    class_count = 0
    basket = request.session.get('basket', {})

    for class_id, class_count in basket.items():
        booking = get_object_or_404(Class_Type, pk=class_id)
        grand_total = class_count * booking.cost
        class_count += grand_total
        basket_items.append({
            'class_id': class_id,
            'class_count': class_count,
            'Class_Type': Class_Type,
        })

    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'class_count': class_count,
    }

    return context