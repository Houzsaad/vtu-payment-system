from django.urls import path
from . views import buy_airtime, buy_data, confirm_transaction
#app_name = 'services'
urlpatterns = [
    path('buy_airtime/', buy_airtime, name='buy_airtime'),
    path('buy_data/', buy_data, name='buy_data'),
    path('confirm_transaction/', confirm_transaction, name='confirm_transaction'),
]
