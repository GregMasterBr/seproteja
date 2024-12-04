from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def home(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'index.html')

def estatisticas(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'estatisticas.html')


def educacional(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'educacional.html')


def denuncias(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'denuncias.html')

def delegacias(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'delegacias.html')