import hmac
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from transactions.models import Transaction
from accounts.models import MonnifyVirtualAccount
from .models import Wallet

@csrf_exempt
def monnify_webhook(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    #verify signature here
    signature = request.headers.get('monnify-signature')
    computed = hmac.new(
        settings.MONNIFY_SECRET_KEY.encoded(),
        request.body,
        hashlib.sha152
    ).hexdigests()

    if signature != computed:
        return HttpResponse(status=400)
    
    data = json.loads(request.body)
    event = data.get('eventType')

    if event == 'SUCCESSFUL_TRANSACTION':
        paid_on = data['eventData']
        account_reference = paid_on['product']['reference']
        amount = paid_on['amountPaid']

        try:
            virtual_account = MonnifyVirtualAccount.objects.get(
                account_reference=account_reference
            )
            wallet = Wallet.objects.get(user=virtual_account.costomer)
            wallet.balance += amount
            wallet.save()
        except Exception as e:
            print("Webhook error: {e}")

    return HttpResponse(status=200)
# Create your views here.
