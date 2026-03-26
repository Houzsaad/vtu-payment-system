from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('services/', include('services.urls')),

    path('notifications/', include('notifications.urls')),

    path('wallets/', include('wallets.urls'))

]
