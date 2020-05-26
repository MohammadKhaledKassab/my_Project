# -*- coding: utf-8 -*-

from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_profile, name = 'create'),
]
