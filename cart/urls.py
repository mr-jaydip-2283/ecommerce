from django.urls import path
from .views import cart_items, add_cart_form

urlpatterns = [
    path('cart/', cart_items, name='cart-items'),
    path('add-cart/', add_cart_form, name='add-cart'),
]
