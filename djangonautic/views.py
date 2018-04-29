from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
    # return HttpResponse("Home")

def sobre(request):
    return render(request, "sobre.html")
    # return HttpResponse("Sobre")