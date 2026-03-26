from django.contrib import admin
from .models import ServiceCategory, ServiceProvider, ServicesPlan, ServicesRequest

admin.site.register(ServiceCategory)
admin.site.register(ServiceProvider)
admin.site.register(ServicesPlan)
admin.site.register(ServicesRequest)
# Register your models here.
