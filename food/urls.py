from django.urls import path
from . views import *
app_name='something'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani'),
]