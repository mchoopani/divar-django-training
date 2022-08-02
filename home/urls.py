from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('call/', call_with_us, name='call')
]
