from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from orders.views import refresh_cart_count
from products.views import HomeListView
from carts.views import checkout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', include('admin_panel.urls')),
    path('accounts/', include('accounts.urls')),
    path('', HomeListView.as_view(), name='index'),
    path('', include('products.urls')),
    path('search/', include('search.urls')),
    path('address/', include('address.urls')),
    path('checkout/', checkout, name='checkout'),
    path('refresh-cart-count/', refresh_cart_count, name='cart_products_count'),
    path('', include('carts.urls')),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)