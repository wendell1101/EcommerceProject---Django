from django.urls import path
from .views import (
    order_success, 
    order_progress, 
    OrderListView,
    order_detail,
)

app_name = 'order'
urlpatterns = [
    path('order/success/', order_success, name="success"),
    path('order/progress/', order_progress, name="progress"),
    path('order/detail/<str:order_id>/', order_detail, name="detail"),
    path('active/orders/', OrderListView.as_view(), name="list"),
]
