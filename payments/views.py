from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from payments.models import Payment
from orders.models import Order

@login_required
def payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,order_id=order_id)    
   
    if order:
        payment = Payment.objects.create(user=request.user, amount=order.order_total)
        payment.save() 
        order.status = 'paid'
        order.save()
        context = {
            'order_total': order.order_total,
        }
    return render(request, 'payments/payment.html', context)

