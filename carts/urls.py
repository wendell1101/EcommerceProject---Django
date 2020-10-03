from django.urls import path
from .views import (
    cart, 
    cart_update,
    add_quantity,
    minus_quantity,
    remove_product_from_cart,
    checkout,
)
app_name = 'cart'

urlpatterns = [
    path('cart-home/', cart, name="home"),
    path('cart-update/<slug>/', cart_update, name="update"),
    path('cart-add-quantity/<slug>/', add_quantity, name="add_quantity"),
    path('cart-minus-quantity/<slug>/', minus_quantity, name="minus_quantity"),
    path('cart-remove-product/<slug>/', remove_product_from_cart, name="remove_product_from_cart"),
]
