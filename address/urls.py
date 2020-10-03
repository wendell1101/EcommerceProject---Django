from django.urls import path
from .views import billing_address, shipping_address

app_name = 'address'
urlpatterns = [
    path('billing/',billing_address, name="billing"),
    path('shipping/',shipping_address, name="shipping"),
]
