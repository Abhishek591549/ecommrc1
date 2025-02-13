from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # ✅ Homepage (Product section)
from django.shortcuts import render

def contact_view(request):
    return render(request, "contact.html")  # ✅ Ensure `contact.html` exists inside `templates/`
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Example Data
    orders = [
        {"order_id": 101, "status": "Delivered"},
        {"order_id": 102, "status": "Pending"},
        {"order_id": 103, "status": "Cancelled"},
    ]

    payments = [
        {"order_id": 101, "amount": 49.99, "status": "Completed"},
        {"order_id": 102, "amount": 29.99, "status": "Pending"},
    ]

    deliveries = [
        {"order_id": 101, "customer": "John Doe", "estimated_date": "2025-02-15", "status": "Out for delivery"},
        {"order_id": 102, "customer": "Jane Doe", "estimated_date": "2025-02-17", "status": "Processing"},
    ]

    context = {
        "user": request.user,
        "total_orders": len(orders),
        "pending_orders": sum(1 for o in orders if o["status"] == "Pending"),
        "delivered_orders": sum(1 for o in orders if o["status"] == "Delivered"),
        "cancelled_orders": sum(1 for o in orders if o["status"] == "Cancelled"),
        "payments": payments,
        "deliveries": deliveries,
    }
    
    return render(request, '/dashboard.html', context)
from django.shortcuts import render
from django.shortcuts import render

def productspage(request):  # Function name should be 'productspage'
    return render(request, 'productspage.html')  # Ensure template exists
