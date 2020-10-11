from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
)
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    View,
)

from orders.models import Order
from products.models import Product
from payments.models import Payment
from customer_profiles.models import CustomerProfile
from address.models import BillingAddress, ShippingAddress  

User = get_user_model()

class AdminView(LoginRequiredMixin,UserPassesTestMixin,View):
    
    def test_func(self):
        return self.request.user.is_admin 
    
    def get(self, *args, **kwargs):
        request = self.request
        context = {
            'orders_count': Order.objects.all().count(),
            'products_count': Product.objects.all().count(),
            'users_count': User.objects.all().count(),
            'payments_count': Payment.objects.all().count(),
        }
        return render(request,'admin_panel/pages/dashboard.html', context)

#users
class UserListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = User
    template_name = 'admin_panel/pages/users.html'
    context_object_name = 'users'
    paginate_by = 10
    order_by = ['is_admin']

    def get_context_data(self, **kwargs):
        context = super(UserListView,self).get_context_data(**kwargs)
        context["id"] = 1
        return context
    
    def test_func(self):
        return self.request.user.is_admin 
# USER CREATE VIEW
class UserCreateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = User
    template_name = 'admin_panel/pages/user_create_form.html'
    fields = ['first_name', 'last_name', 'email', 'is_admin']
    success_url = reverse_lazy('admin_panel:users')
    success_message = 'A user has been created successfully'
    
    def test_func(self):
        return self.request.user.is_admin 

#USER UPDATE VIEW
class UserUpdateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = User
    template_name = 'admin_panel/pages/user_create_form.html'
    fields = ['first_name', 'last_name', 'email', 'is_admin']
    success_url = reverse_lazy('admin_panel:users')
    success_message = 'A user has been updated successfully'
    
    orders = Order.objects.all()
    user_list = []
    
    def test_func(self):
        return self.request.user.is_admin 

#User Delete view
class UserDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'admin_panel/pages/user_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:users')
    success_message = 'A user has been deleted successfully'
    
    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_admin 


    
#ProductsListView    
class ProductListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Product
    template_name = 'admin_panel/pages/products.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        orders = Order.objects.all()
        product_list = []
        for order in orders:
            for product in order.cart.products.all():
                product = product
                product_list.append(product)
        print(product_list)
        context["product_list"] = product_list
        return context
    
    def test_func(self):
        return self.request.user.is_admin 

#ProductDeleteView
class ProductDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Product
    template_name = 'admin_panel/pages/product_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:products')
    success_message = 'An item has been deleted successfully'
    
    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ProductDeleteView, self).delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_admin 

#ProductCreateView
class ProductCreateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Product
    template_name = 'admin_panel/pages/product_create_form.html'
    fields = ['title', 'price','discount_percent', 'category', 'label', 'description', 'image1']
    success_url = reverse_lazy('admin_panel:products')
    success_message = 'An item has been created successfully'
    
    def test_func(self):
        return self.request.user.is_admin 

class ProductUpdateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Product
    template_name = 'admin_panel/pages/product_create_form.html'
    fields = ['title', 'price', 'category', 'label', 'description', 'image1']
    success_url = reverse_lazy('admin_panel:products')
    success_message = 'An item has been updated successfully'
    
    def test_func(self):
        return self.request.user.is_admin 

#orders
#Order List View
class OrderListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Order
    template_name = 'admin_panel/pages/orders.html'
    context_object_name = 'orders'
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_admin 

#Order Update View
class OrderUpdateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Order
    template_name = 'admin_panel/pages/order_update_form.html'
    fields = ['status',]
    success_url = reverse_lazy('admin_panel:orders')
    success_message = 'An order has been updated successfully'
    
    def test_func(self):
        return self.request.user.is_admin 


    
    
class PaymentListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Payment
    template_name = 'admin_panel/pages/payments.html'
    context_object_name = 'payments'
    paginate_by = 10
    ordering = ['-timestamp']
    
    def test_func(self):
        return self.request.user.is_admin 
    





