from django.contrib import admin
from django.urls import path, include
from services.views import home

urlpatterns = [

    path('admin/', admin.site.urls),

<<<<<<< HEAD
    path('', include('accounts.urls')),

    #path('', home, name='home'),
    
=======
    path('', home, name='home'),

    path('accounts/', include('accounts.urls')),

>>>>>>> fe80a850a364d529771be31eab55158a9c160e92
    path('services/', include('services.urls')),

    path('notifications/', include('notifications.urls')),

    path('wallets/', include('wallets.urls'))

]
