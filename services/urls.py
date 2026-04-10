from django.urls import path
from . views import buy_airtime, buy_data, confirm_transaction, transaction_history
#app_name = 'services'
urlpatterns = [
    path('buy_airtime/', buy_airtime, name='buy_airtime'),
    path('buy_data/', buy_data, name='buy_data'),
    path('confirm_transaction/', confirm_transaction, name='confirm_transaction'),
    path('transaction_history/', transaction_history, name='transaction_history')
<<<<<<< HEAD

=======
>>>>>>> fe80a850a364d529771be31eab55158a9c160e92
]
