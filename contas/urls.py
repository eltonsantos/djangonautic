from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registrar

app_name = 'contas'

urlpatterns = [
    path('registrar/', registrar, name='registrar'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]