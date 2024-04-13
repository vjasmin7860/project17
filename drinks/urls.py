from django.urls import path
from drinks.views import *
app_name='drinks'
urlpatterns=[
    path('mazza/',mazza,name='mazza'),
    path('sprit/',sprit,name='sprit'),
]