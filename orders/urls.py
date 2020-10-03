from django.urls import path
from .views import order_success

app_name = 'order'
urlpatterns = [
    path('order/success/', order_success, name="success"),
]
