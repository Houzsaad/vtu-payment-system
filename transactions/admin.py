from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = (
        'transaction_type',
        'phone_number',
        'network',
        'amount',
        'status',
        'created_at'
    )