from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all().values()
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)
