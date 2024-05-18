from django.shortcuts import render
from store.models import Product
import random

def home(request):
    products = random.choices(Product.objects.all().filter(is_available=True), k=32)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)