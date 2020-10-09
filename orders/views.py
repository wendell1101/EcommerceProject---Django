import math
from datetime import timedelta
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView


from orders.models import Order
from carts.models import Cart
from payments.models import Payment

def order_success(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,order_id=order_id)
 
    if order:
        del request.session['cart_id']         
        del request.session['cart_items_count']

    context = {
        'order':order,
    }
    return render(request, 'orders/order_success.html', context)


def order_progress(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,order_id=order_id)
    order.ordered_date += timedelta(days=7,hours=0)
    delivery_time = order.ordered_date
    print(delivery_time)
    if order:
        del request.session['cart_id']      
        if request.session.get('cart_items_count'):   
            del request.session['cart_items_count']
    if request.is_ajax():
        data = {
            "cartCount": request.session.get('cart_items_count')
        }
        return JsonResponse(data)
    context = {
        'order': order,
        'delivery_time': delivery_time,
    }
    return render(request, 'orders/order_progress.html', context)

def order_detail(request,order_id):
    order = get_object_or_404(Order,order_id=order_id)
    order.ordered_date += timedelta(days=7,hours=0)
    delivery_time = order.ordered_date
    context = {
        'order':order,
        'delivery_time': delivery_time,
    }
    return render(request,'orders/order_detail.html',context)

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
   
