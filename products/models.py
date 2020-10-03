from django.db import models
from django.db.models.signals import pre_save,post_save
from ecommerce_project.utils import unique_slug_generator
from django.shortcuts import reverse

import math
import random
import os

CATEGORY_CHOICES = (
    ('none','None'),
    ('shirt','Shirt'),
    ('dress','Dress'),
    ('shoes','Shoes'),
    ('phone','Phone'),
    ('laptop','Laptop'),
    ('accessories','Accessories'),
)

LABEL_CHOICES = (
    ('none','NONE'),
    ('new','NEW'),
    ('hot','HOT'),
    ('special','SPECIAL'),
    ('best_seller','BEST SELLER'),
)

class Product(models.Model):
    title               = models.CharField(max_length=100)
    slug                = models.SlugField()
    quantity            = models.IntegerField(default=1)
    price               = models.DecimalField(max_digits=2000000, decimal_places=2)
    discount_percent    = models.DecimalField(max_digits=3,decimal_places=2, blank=True, default=0)
    category            = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default="none")
    label               = models.CharField(choices=LABEL_CHOICES, max_length=100, default="none")
    description         = models.TextField()
    timestamp           = models.DateTimeField(auto_now_add=True)
    image1              = models.ImageField(default="default_product_image.jpg", upload_to="products", blank=True)
    image2              = models.ImageField(default="default_product_image.jpg", upload_to="products", blank=True)    
    image3              = models.ImageField(default="default_product_image.jpg", upload_to="products", blank=True)
    image4              = models.ImageField(default="default_product_image.jpg", upload_to="products", blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug": self.slug})
    
    def get_final_price(self):
        if self.discount_percent:
            price = self.get_discounted_price()
        else:
            price = self.price
        return price
    
    def get_final_total_price(self):
        if self.discount_percent:
            discounted_price = self.get_discounted_price()
            total = math.prod([discounted_price, self.quantity])
        else:
            total = math.prod([self.price, self.quantity])
        return total
            
    def get_discounted_price(self):
        discount = self.price * self.discount_percent 
        discounted_price = self.price - discount
        return discounted_price
    
    def get_discount_percent(self):
        return self.discount_percent * 100
    
    def get_label_color(self):
        if self.label == 'new':
            return 'primary'
        elif self.label == 'hot':
            return 'danger'
        elif self.label == 'special':
            return 'info'
        elif self.label == 'best_seller':
            return 'success'
        else:
            pass
    
#signals
def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
    
