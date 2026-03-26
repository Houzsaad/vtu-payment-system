from django.db import models
from django.conf import settings
import uuid

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True) #data and airtime
    slug = models.SlugField(unique=True) #data and airtime
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='providers'
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    vtpass_services_id = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} - {self.category.name}"

class ServicesPlan(models.Model):
    provider = models.ForeignKey(
        ServiceProvider,
        on_delete=models.CASCADE,
        related_name='plan'
    )
    name = models.CharField(max_length=100)
    vtpass_variation_code = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    validity = models.CharField(max_length=50, null=True, blank=True)
    #vtpass_service_id = models.ChaField(max_length=100)
    is_active = models.BooleanField(default=True) #30 days
    def __str__(self):
        return f"{self.provider.name} | {self.name} | ${self.amount}"

class ServicesRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESS = 'success', 'Success'
        FAILED = 'failed', 'Failed'

    reference = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='services_requests'
    )
    plan = models.ForeignKey(
        ServicesPlan,
        on_delete=models.SET_NULL,
        null=True,
        related_name='requests'
    )
    phone_numberc = models.CharField(max_length=11)
    amount = models.DecimalField(max_digits=12, decimal_places=2)       
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )
    vtpass_response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.plan} | {self.status}"
# Create your models here.
