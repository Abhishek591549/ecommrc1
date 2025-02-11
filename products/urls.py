from django.urls import path
from . import views
# ✅ Fix import (use correct structure)
from .views import contact_view  
from .views import dashboard_view  # 
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    
    #
   
  
   
]
