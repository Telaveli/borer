from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index),
    path('generic/', views.generic),
    path('elements/', views.elements)
]
