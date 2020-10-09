from django.urls import path
from .views import (
    admin, 
    CustomerListView, 
    ProductListView, 
    OrderListView,
    PaymentListView,
)

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/',admin , name='dashboard'),
    path('customers/',CustomerListView.as_view() , name='customers'),
    path('products/',ProductListView.as_view() , name='products'),
    path('orders/',OrderListView.as_view() , name='orders'),
    path('payment/',PaymentListView.as_view() , name='payments'),
]
