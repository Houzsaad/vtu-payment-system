from django.urls import path
from .views import register, login, dashboard, logout, profile
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile')
]
