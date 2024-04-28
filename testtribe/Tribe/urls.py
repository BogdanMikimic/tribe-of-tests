from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('story', story, name='story'),
    path('my_notes', my_notes, name='my_notes')
]
