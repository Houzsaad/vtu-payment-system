from django.db import models
from django.conf import settings
from decimal import Decimal

#User = settings.AUTH.USER.MODEL



class Wallet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wallet'
    )

    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def deposit(self, amount):
        if amount <= 50:
            raise ValueError('Deposit must be greater than 50')
        self.balance += amount
        self.save()

    def __str__(self):
        return f"{self.user.email} - ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('withdraw must NOT be 0 ')

        if self.balance < amount:
            raise ValueError('isfcnt fund')
        self.balance -= amount
        self.save()

    