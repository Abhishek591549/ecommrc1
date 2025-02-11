from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, logout_view  # ✅ Import views

from .views import home_view


from .views import products_view,  orders_view, payment_view
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .views import product_view, add_to_cart, view_cart, remove_from_cart

from django.contrib.auth.models import User


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('testimonial/', views.testimonial, name='testimonial'),
 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', home_view, name='home'),  
    path('products/', products_view, name='products'),
   
    path('orders/', orders_view, name='orders'),
    path('payment/', payment_view, name='payment'),
     path('dashboard/', views.dashboard_view, name='dashboard'),  # ✅ Ensure this exists
     path('settings/', views.settings_view, name='settings'),
      path("products/", product_view, name="product_page"),  # Display products in product.html
    path("products/<int:product_id>/add-to-cart/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="view_cart"),
    path("cart/remove/<int:cart_item_id>/", remove_from_cart, name="remove_from_cart"),
      path("products/", views.product_page, name="product_page"),  
  
   
    
    
    
    
    

    
    
    ]