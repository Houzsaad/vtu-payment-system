from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wallet
from django.conf import settings
from accounts.models import Costomer, MonnifyVirtualAccount
from accounts.monnify import create_virtual_account

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

        try:
            data = create_virtual_account(instance)
            response_body = data['responseBody']
            accounts = response_body['accounts']

            MonnifyVirtualAccount.objects.create(
                costomer=instance,
                account_number=accounts[0]['accountNumber'],
                bank_name=response_body['accountName'],
                account_reference=response_body['accountReference']
            )
        except Exception as e:
            print(f"Monnify virtual account creation failed: {e}")
        #MonnifyVirtualAccount.objects.create(costomer=instance)