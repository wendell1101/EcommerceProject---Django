from django.shortcuts import render
from django.views.generic import ListView, DetailView


from carts.models import Cart
from .models import Product

class HomeListView(ListView):
    model = Product
    template_name = 'pages/index.html'
    context_object_name = 'products'
    paginate_by = 1
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context



