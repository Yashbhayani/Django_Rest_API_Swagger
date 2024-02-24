from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', API.as_view())
]