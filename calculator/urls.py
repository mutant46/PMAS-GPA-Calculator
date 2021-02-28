from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.caculate, name='calculate'),
]