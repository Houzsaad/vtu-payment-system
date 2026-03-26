from django.db import models
from django.conf import settings
from decimal import Decimal
import uuid
from wallets.models import Wallet

User = settings.AUTH_USER_MODEL

class Transaction(models.Model):
   
    class TransactionType(models.TextChoices):
        DEPOSIT = 'DEPOSIT', 'Deposit'
        BUY_AIRTIME = 'BUY_AIRTIME', 'Airtime'
        BUY_DATA = 'BUY_DATA', 'Data'
        WITHDRAWAL = 'WITHDRAWAL', 'Withdrawal'
        VTU_PURCHASE = 'VTU_PURCHASE', 'VTU Purchase'
        BILL_PAYMENT = 'BILL_PAYMENT', 'Bill Payment'

    class TransactionStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'
        
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name = 'transactions'
    )


    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionType.choices
    )


    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=TransactionStatus.choices,
        default=TransactionStatus.COMPLETED
    )

    #phone_number = models.CharField(max_length=11, null=True, blank=True), #beneficiary
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=15),
    phone_number = models.CharField(max_length=11, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] #lasttest trxns come first
    
    def __str__(self):
        return f"{self.transaction_type} - ${self.amount} - {self.reference_id} - {self.phone_number}"




# Create your models here.
