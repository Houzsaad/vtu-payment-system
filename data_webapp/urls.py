from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
#from django.http import HttpResponse
from .views import home
#def home (request):
#   return HttpResponse('hey')

urlpatterns = [
    path('', home, name='home'),

    path('accounts/', include('accounts.urls')),

    path('admin/', admin.site.urls),

    path('services/', include('services.urls')),

    path('notifications/', include('notifications.urls')),

    path('wallets/', include('wallets.urls'))

]
