from django.shortcuts import render

def landing(request):
    context = {}
    return render(request, "landing.html", context=context)

def index(request):
    context = {}
    return render(request, "index.html", context=context)

def register(request):
    context = {}
    return render(request, "register.html", context=context)

def login_view(request):
    context = {}
    return render(request, "login.html", context=context)

def convert(request):
    context = {}
    return render(request, "convert.html", context=context)


