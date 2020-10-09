from django.shortcuts import render
from django.views.generic import ListView

from orders.models import Order
from products.models import Product
from payments.models import Payment
from customer_profiles.models import CustomerProfile
from address.models import BillingAddress, ShippingAddress  

def admin(request):
    return render(request,'admin_panel/pages/dashboard.html')

class CustomerListView(ListView):
    model = CustomerProfile
    template_name = 'admin_panel/pages/customers.html'
    context_object_name = 'customers'
    paginate_by = 10


class ProductListView(ListView):
    model = Product
    template_name = 'admin_panel/pages/products.html'
    context_object_name = 'products'
    paginate_by = 10

class OrderListView(ListView):
    model = Order
    template_name = 'admin_panel/pages/orders.html'
    context_object_name = 'orders'
    paginate_by = 10
    
class PaymentListView(ListView):
    model = Payment
    template_name = 'admin_panel/pages/payments.html'
    context_object_name = 'payments'
    paginate_by = 10
    ordering = ['-timestamp']





