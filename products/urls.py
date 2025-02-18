from django.urls import path
from . import views
# ✅ Fix import (use correct structure)
from .views import contact_view  
from .views import dashboard_view  
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('productspage/', views.productspage, name='productspage'),  # Ensure function name matches views.py
   path('my-orders/', views.my_orders_view, name='my_orders'),  # List all orders
    path('order-details/<int:order_id>/', views.order_details_view, name='order_details'),  # View order details

    
    
   
  
   
]
