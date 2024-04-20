from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<class_id>', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:item_id>/', views.remove_from_basket,
         name='remove_from_basket'),
]
