from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription, name='subscription'),
    path('checkout/', views.subscribe, name='checkout'),
]