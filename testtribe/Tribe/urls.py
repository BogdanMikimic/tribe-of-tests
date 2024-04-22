from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('img_credits', img_credits, name='img_credits'),
]
