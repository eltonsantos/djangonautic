from django.shortcuts import render
from .models import Artigo
from django.http import HttpResponse

def artigos(request):
    artigos = Artigo.objects.all().order_by('data')
    return render(request, "artigos.html",  {'artigos' : artigos})

def detalhes(request, slug):
    artigo = Artigo.objects.get(slug=slug)
    return render(request, 'detalhes.html', {'artigo' : artigo})
    #return HttpResponse(slug)