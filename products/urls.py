from django.urls import path
from .views import (
    ProductDetailView, 
    LaptopListView,
    AccessoryListView,
    PhoneListView,
)

app_name = "product"
urlpatterns = [
    path('product-detail/<slug>/', ProductDetailView.as_view(), name="detail"),
    path('products/laptops/', LaptopListView.as_view(), name="laptop_list"),
    path('products/phones/', PhoneListView.as_view(), name="phone_list"),
    path('products/accessories/', AccessoryListView.as_view(), name="accessory_list"),
]
