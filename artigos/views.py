from django.shortcuts import render

def artigos(request):
    return render(request, "artigos.html")