from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')  # ✅ Homepage

def about(request):
    return render(request, 'about.html')  # ✅ About Page

def contact(request):
    return render(request, 'contact.html')  # ✅ Contact Page

def blog_list(request):
    return render(request, 'blog_list.html')  # ✅ Blog List Page

def testimonial(request):
    return render(request, 'testimonial.html')  # ✅ Testimonial Page
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Login View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:  # ✅ Only log in if user exists
           messages.error(request, "Invalid email or password.")  # ✅ Redirect to the dashboard
        else:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to Dashboard...")
            print("✅ User authenticated and logged in:", user)  # Debugging
            return redirect("/dashboard")  # Redirect to the dashboard
            # ✅ Prevent AnonymousUser error

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration successful! Redirecting to login page...")
            return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("login")
from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')
from django.shortcuts import render

def products_view(request):
    return render(request, 'index.html')


def orders_view(request):
    return render(request, 'orders.html')

def payment_view(request):
    return render(request, 'payment.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def settings_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        user = request.user
        user.username = username
        user.email = email

        if password and password == confirm_password:
            user.set_password(password)

        user.profile.phone = phone
        user.profile.address = address
        user.save()

        return redirect('dashboard')

    return render(request, 'settings.html')





from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # ✅ Ensures only logged-in users can access the dashboard
def dashboard_view(request):
    return render(request, "dashboard.html")  # ✅ Make sure "dashboard.html" exists
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, CartItem  # Ensure these models exist in accounts/models.py

def product_view(request):
    """ Display all products on a single page (product.html) """
    products = Product.objects.all()  
    return render(request, "/product.html", {"products": products})

@login_required
def add_to_cart(request, product_id):
    """ Add a product to the cart """
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Product added to cart successfully!")
    return redirect("product_page")  # Redirect to the same product.html page

@login_required
def view_cart(request):
    """ View all items in the cart """
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "accounts/product.html", {"products": Product.objects.all(), "cart_items": cart_items})

@login_required
def remove_from_cart(request, cart_item_id):
    """ Remove an item from the cart """
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect("product_page")  # Redirect to the same product.html page
from django.shortcuts import render

def product_page(request):
    return render(request, "product.html")  # ✅ Ensure 'product.html' exists in the templates folder
