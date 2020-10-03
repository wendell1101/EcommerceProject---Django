import math
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from carts.models import Cart

def order_success(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,order_id=order_id)
    if order:
        del request.session['cart_id']
        request.session['cart_items_count'] = cart_obj.products.count()
    # if request.is_ajax():
    #     data = {
    #         'cart_items_count' : cart_obj.products.count()
    #     }
    #     return JsonResponse(data)
        
  
    context = {
        'order':order,
    }
    return render(request, 'orders/order_success.html', context)

def refresh_cart_count(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if request.is_ajax():
        data = {
            'cart_items_count' : cart_obj.products.count()
        }
        return JsonResponse(data)

