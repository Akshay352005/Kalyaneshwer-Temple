from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donations/', views.donations, name='donations'),
    path('services/', views.services, name='services'),
    path('events/', views.events, name='events'),
]
