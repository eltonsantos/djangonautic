from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("artigos:artigos")
    else:
        form = UserCreationForm()
    return render(request, "registrar.html", {'form' : form})

def login(request):
    return render(request, "login.html")
