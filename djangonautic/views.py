from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def sobre(request):
    return HttpResponse("Sobre")