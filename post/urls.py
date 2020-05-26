# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
#DataFlair #AJAX tutorial
        path('', views.index, name='index'),
        path('like/', views.like, name='like'), ]