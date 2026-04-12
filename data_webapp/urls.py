from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
#from django.http import HttpResponse

#def home (request):
#   return HttpResponse('hey')

urlpatterns = [

    path('', lambda request: redirect('login'), name='home'),

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    
    #path('', home, name='home'),

    path('services/', include('services.urls')),

    path('notifications/', include('notifications.urls')),

    path('wallets/', include('wallets.urls'))

]
