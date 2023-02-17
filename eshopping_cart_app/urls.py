from django.urls import path

from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('item_decrement/<int:product_id>/', views.cart_item_quantity, name='item_decrement'),
    path('item_delete/<int:product_id>/', views.cart_item_delete, name='item_delete'),
]
