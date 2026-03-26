from django.urls import path
from .views import home
urlpatterns = [
    #path('', accounts, name('accounts.urls'))
    path('', home, name='home'),
]
