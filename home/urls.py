from django.urls import path
from . import views
#from example.core import views as core_views

urlpatterns = [
    path('', views.index, name='home'),
    path("favicon.ico", views.favicon),
]
