from django.urls import path
from .views import add_product, decrement_product, clear_cart, remove_product

app_name = "cart"

urlpatterns = [
    path('clear/', clear_cart, name='clear_cart'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
]
