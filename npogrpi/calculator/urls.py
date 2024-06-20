from django.urls import path

from . import views

app_name = 'calculator'

urlpatterns = [
    path('calculator/', views.product_search, name='product_search'),
    path('mgrp/', views.mgrp, name='mgrp')
]