from django.urls import path
from . import views

urlpatterns = [
    path('products-view/', views.products_view, name='products-view'),
    path('create-products/', views.create_products, name='create-products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('chatbot/', views.chatbot_view, name='chatbot')
]
