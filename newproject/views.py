from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def testimonial(request):
    return render(request, 'testimonial.html')

def blog_list(request):
    return render(request, 'blog_list.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def productspage(request):
    return render(request, 'productspage.html')  # Render productspage template
