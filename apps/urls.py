from django.urls import path, include

urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('orders/', include('apps.orders.urls')),
    path('', include('apps.products.urls')),
    path('', include('apps.cart.urls')),
]
