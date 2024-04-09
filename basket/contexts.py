from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    class_count = 0

    context = {
        'basket_items': basket_items,
        'total': total,
        'class_count': class_count,
    }

    return context