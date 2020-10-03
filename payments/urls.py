from django.urls import path
from .views import payment

app_name = 'payment'
urlpatterns = [
    path('payment/paypal/', payment, name="paypal"),
]
