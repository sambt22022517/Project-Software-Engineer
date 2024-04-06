from django.http import HttpResponse
from django.template import loader
from .models import User


def sign_up(request):
    template = loader.get_template("sign_up.html")
    return HttpResponse(template.render(request=request))

def sign_in(request):
    template = loader.get_template("sign_in.html")
    return HttpResponse(template.render(request=request))

def home(request):
    template = loader.get_template("home.html")
    context = {
        'user': User.objects.all().values(),
    }
    return HttpResponse(template.render(request=request, context=context))

def signup(request):
    username = request.GET['username']
    telephone = request.GET['telephone']
    password = request.GET['password']
    repassword = request.GET['re-password']

    User(username=username, telephone=telephone, password=password).save()

    template = loader.get_template("home.html")
    context = {
        'user': User.objects.all().values(),
    }
    return HttpResponse(template.render(request=request, context=context))

def signin(request):
    user_phone = request.GET['user_phone']
    password = request.GET['password']

    user = User.objects.all().values()

    template = loader.get_template("home.html")
    context = {
        'user' : user, 
    }
    return HttpResponse(template.render(request=request, context=context))