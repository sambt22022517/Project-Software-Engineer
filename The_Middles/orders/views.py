from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    template = loader.get_template('cart/gio-hang-da-dang-nhap.html')
    context = {
        'lst' : range(10)
    }
    return HttpResponse(template.render(context, request))