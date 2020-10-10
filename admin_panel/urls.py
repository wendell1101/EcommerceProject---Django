from django.urls import path
from .views import (
    AdminView, 
    UserListView, 
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    ProductListView, 
    OrderListView,
    OrderUpdateView,
    PaymentListView,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView,
)

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/',AdminView.as_view() , name='dashboard'),
    path('users/',UserListView.as_view() , name='users'),
    path('user/create/',UserCreateView.as_view() , name='user_create'),
    path('user/update/<int:pk>/',UserUpdateView.as_view() , name='user_update'),
    path('user/delete/<int:pk>/',UserDeleteView.as_view() , name='user_delete'),
    path('products/',ProductListView.as_view() , name='products'),
    path('delete/product/<slug>/',ProductDeleteView.as_view() , name='product_delete'),
    path('create/product/',ProductCreateView.as_view() , name='product_create'),
    path('update/product/<slug>/',ProductUpdateView.as_view() , name='product_update'),
    path('orders/',OrderListView.as_view() , name='orders'),
    path('orders/update/<pk>/',OrderUpdateView.as_view() , name='order_update'),
    path('payment/',PaymentListView.as_view() , name='payments'),
]
