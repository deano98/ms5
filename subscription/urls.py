from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription, name='subscription'),
    path('subscribe/', views.subscription, name='subscribe'),
]