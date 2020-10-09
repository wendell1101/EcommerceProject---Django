from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Cart
from products.models import Product
from address.models import BillingAddress, ShippingAddress
from address.forms import BillingAddressForm, ShippingAddressForm
from orders.models import Order
from orders.forms import OrderForm
from customer_profiles.models import CustomerProfile


def cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    context = {
        'cart' : cart_obj
    }
    return render(request,'carts/cart.html',context)

def cart_update(request, slug):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
            added = True
            product_obj.quantity = 1
            product_obj.save()
        request.session['cart_items_count'] = cart_obj.products.count()

        #ajax
        if request.is_ajax():
            products = [{
                "id" : x.id,
                "name": x.title,
                "image": x.image1.url,
                "quantity": x.quantity,
                "price":x.get_final_price(),
                "discount": x.get_discount_percent(),
                "total": x.get_final_total_price(),
            } 
            for x in cart_obj.products.all()]
            data = {
                "added": added,
                'removed': not added,
                "cartItemCount": request.session.get('cart_items_count'),
                "quantity": product_obj.quantity,          
            }
            return JsonResponse(data)
    return redirect('cart:home')

def remove_product_from_cart(request, slug):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product = get_object_or_404(Product,slug=slug)    
    if product in cart_obj.products.all():
        cart_obj.products.remove(product)
        cart_obj.save()
        request.session['cart_items_count'] = cart_obj.products.count()
        
    return redirect('cart:home')

def add_quantity(request,slug):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product = get_object_or_404(Product,slug=slug)    
    if product.quantity > 0:
        product.quantity +=1
        product.save()
    
    return redirect('cart:home')

def minus_quantity(request,slug):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product = get_object_or_404(Product,slug=slug)    
    if product.quantity > 1:
        product.quantity -=1
        product.save()
        
    return redirect('cart:home')

@login_required
def checkout(request):    
    cart_obj, new_obj = Cart.objects.new_or_get(request)            
    try:
        customer_profile = get_object_or_404(CustomerProfile, user=request.user)
        form = OrderForm(initial={'payment_type': 'cod'})
        if request.method == "POST":
            form = OrderForm(request.POST)
            payment_type= request.POST.get('payment_type')
            if payment_type == 'cod':
                order = Order(
                    customer_profile    = customer_profile,
                    cart                = cart_obj,
                    billing_address     = BillingAddress.objects.filter(customer_profile=customer_profile).first(),
                    shipping_address    = ShippingAddress.objects.filter(customer_profile=customer_profile).first(),
                    status              = 'created',
                    order_total         = cart_obj.get_cart_total(),
                    payment_type        = payment_type,
                )
                order.status = 'created'
                
                order.save()
                request.session['order_id'] = order.order_id
                return redirect('order:progress')
            elif payment_type == 'paypal':     
                order = Order(
                    customer_profile    = customer_profile,
                    cart                = cart_obj,
                    billing_address     = BillingAddress.objects.filter(customer_profile=customer_profile).first(),
                    shipping_address    = ShippingAddress.objects.filter(customer_profile=customer_profile).first(),
                    status              = 'created',
                    order_total         = cart_obj.get_cart_total(),
                    payment_type        = payment_type,
                )
                order.save()        
                request.session['order_id'] = order.order_id
                return redirect('payment:paypal')
            
    except ObjectDoesNotExist:
        pass
    context = {
        'cart' : cart_obj,
        'form' : form,  
    }
    return render(request, 'pages/checkout.html', context)


