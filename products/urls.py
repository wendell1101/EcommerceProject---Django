from django.urls import path
from .views import ProductDetailView

app_name = "product"
urlpatterns = [
    path('product-detail/<slug>/', ProductDetailView.as_view(), name="detail"),
]
