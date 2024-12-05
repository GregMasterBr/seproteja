from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('educacional/', views.educacional, name='educacional'),
    path('denuncias/', views.denuncias, name='denuncias'),
    path('delegacias-ciberneticas/', views.delegacias, name='delegacias'),
]

