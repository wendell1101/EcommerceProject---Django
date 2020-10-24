from django.shortcuts import render
from django.views.generic import ListView, DetailView


from carts.models import Cart
from .models import Product

class HomeListView(ListView):
    model = Product
    template_name = 'pages/index.html'
    context_object_name = 'products'
    # paginate_by = 8

#laptop category

class LaptopListView(ListView):
    model = Product
    template_name = 'pages/laptop_list.html'    
    
    def get_context_data(self, *args, **kwargs):
        context = super(LaptopListView, self).get_context_data(*args, **kwargs)
        context["products"] = Product.objects.filter(category="laptop")
        return context

#phone category
class PhoneListView(ListView):
    model = Product
    template_name = 'pages/phone_list.html'    
    
    def get_context_data(self, *args, **kwargs):
        context = super(PhoneListView, self).get_context_data(*args, **kwargs)
        context["products"] = Product.objects.filter(category="phone")
        return context
    
#Accesories category
class AccessoryListView(ListView):
    model = Product
    template_name = 'pages/accessories.html'    
    
    def get_context_data(self, *args, **kwargs):
        context = super(AccessoryListView, self).get_context_data(*args, **kwargs)
        context["products"] = Product.objects.filter(category="accesories")
        return context
    

    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context



