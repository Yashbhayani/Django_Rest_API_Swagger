from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('hi/', hi),
    path('userdata/', UserAPI.as_view(), name='your-model-list'),
    path('userdata/<int:pk>', UserIDAPI.as_view(), name='your-model-list')
]