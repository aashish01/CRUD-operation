from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('', views.list, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delt/<int:id>', views.delt, name='delt'),
]