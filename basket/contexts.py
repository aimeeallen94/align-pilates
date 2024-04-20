from django.shortcuts import get_object_or_404
from classes.models import Class_Type


def basket_contents(request):

    basket_items = []
    grand_total = 0
    class_count = 0
    cost = 15
    basket = request.session.get('basket', {})

    for class_id, item_data in basket.items():
        if isinstance(item_data, int):
            booking = get_object_or_404(Class_Type, pk=class_id)
            class_count += item_data
            grand_total += class_count * cost
            basket_items.append({
                'class_id': class_id,
                'class_count': item_data,
                'booking': booking,
            })

    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'class_count': class_count,
    }

    return context
