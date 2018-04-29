from django.urls import path
from .views import artigos, detalhes

app_name = 'artigos'

urlpatterns = [
    path('', artigos, name='artigos'),
    path('<slug:slug>', detalhes, name='detalhes'),
]
