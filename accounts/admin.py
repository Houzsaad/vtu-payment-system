from django.contrib import admin

from .models import Costomer

from .models import Costomer, MonnifyVirtualAccount
admin.site.register(Costomer)

admin.site.register(MonnifyVirtualAccount)

# Register your models here.
