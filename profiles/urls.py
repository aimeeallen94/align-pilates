from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile , name='profile'),
    path('reservation_history/<reservation_number>', views.reservation_history , name='reservation_history'),
]
