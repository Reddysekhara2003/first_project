from django.urls import path
from . views import *
app_name='anything'
urlpatterns=[
    path('iphone/',iphone,name='iphone'),
]