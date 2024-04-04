from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")