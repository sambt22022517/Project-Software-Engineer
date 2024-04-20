from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    template = loader.get_template('cart/gio-hang-da-dang-nhap.html')

    # các biến có trong file gio-hang-da-dang-nhap.html được liệt kê hết ở đây
    context = {
        'lst' : range(10),
        'checked':'false',
        'content_review_product': 'This is review',
        'unit_price': '1',
        'total_price': '10',
        'total_product': '10',
        'total_checkout': '1 tỷ',
    }
    return HttpResponse(template.render(context, request))
def test_gio_hang_trong(request):
    template = loader.get_template('cart/gio-hang-trong.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))