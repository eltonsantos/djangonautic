from django.urls import path
from .views import artigos

urlpatterns = [
    path('', artigos),
]
