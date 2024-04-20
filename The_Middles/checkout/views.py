from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

def test_thanh_toan(request):
    template = loader.get_template('checkout/thanh-toan.html')
    context = {
        'lst' : range(10),
    }
    return HttpResponse(template.render(context, request))