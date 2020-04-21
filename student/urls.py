# -*- coding: utf-8 -*-
from . import views
from django.urls import path

urlpatterns = [
    path('', views.student_show, name = 'student_show'),
]