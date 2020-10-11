import math
from django.db import models
from django.conf import settings
from django.db.models.signals import m2m_changed

from products.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products    = models.ManyToManyField(Product)
    timestamp   = models.DateTimeField(auto_now_add=True)
    total       = models.FloatField()
    
    objects = CartManager()
    
    def __str__(self):
        return str(self.id)
    
    def get_cart_total(self):
        total = 0
        for x in self.products.all():
            total = math.fsum([x.get_final_total_price(), total])
        return format(total,'.2f')