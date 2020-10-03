import math
from django.db import models
from django.db.models.signals import pre_save, post_save
from ecommerce_project.utils import unique_order_id_generator

from customer_profiles.models import CustomerProfile
from carts.models import Cart
from address.models import BillingAddress, ShippingAddress

ORDER_STATUS = (
    ('created','CREATED'),
    ('paid','PAID'),
    ('shipped','SHIPPED'),
)
PAYMENT_TYPE = (
    ('cod','CASH ON DELIVERY'),
    ('paypal', 'PAYPAL')
)

class Order(models.Model):
    customer_profile     = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    order_id             = models.CharField(max_length=20)
    cart                 = models.ForeignKey(Cart, on_delete=models.CASCADE)
    billing_address      = models.ForeignKey(BillingAddress, on_delete=models.RESTRICT, null=True, blank=True, related_name='billing_address')
    shipping_address     = models.ForeignKey(ShippingAddress, on_delete=models.RESTRICT, null=True, blank=True, related_name='shipping_address')
    status               = models.CharField(max_length=120,default='created',choices = ORDER_STATUS)
    shipping_price       = models.DecimalField(default=50.00,max_digits=100, decimal_places=2)
    order_total          = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    ordered_date         = models.DateTimeField(auto_now_add=True)    
    active               = models.BooleanField(default=True) #if shipped return false
    payment_type         = models.CharField(max_length=20, choices = PAYMENT_TYPE, default='cod')
    
    def __str__(self):
        return self.order_id


#generate order_id
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(customer_profile=instance.customer_profile)
    if qs.exists():
        qs.update(active=False)
pre_save.connect(pre_save_create_order_id, sender=Order)
