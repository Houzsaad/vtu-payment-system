from django.urls import path
from . import views

urlpatterns = [
    path('webhook/monnify', views.monnify_webhook, name='monnify_webhook')
]
