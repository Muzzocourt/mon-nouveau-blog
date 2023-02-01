# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:15:08 2023

@author: PC
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]