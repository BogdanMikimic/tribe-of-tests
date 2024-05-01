from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('tribe_village', tribe_village, name='tribe_village'),
    path('story', story, name='story'),
    path('workshops', workshops, name='workshops'),
    path('jungle', jungle, name='jungle'),
    path('my_notes', my_notes, name='my_notes')
]
