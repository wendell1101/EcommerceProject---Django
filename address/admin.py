from django.contrib import admin
from .models import BillingAddress, ShippingAddress, DefaultAddress

admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(DefaultAddress)
