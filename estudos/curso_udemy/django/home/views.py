from django.shortcuts import render
from django.http import HttpResponse

# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def home(request):
    print("home") # Pode fazer oque quiser dentro da função
    return HttpResponse('Home do app 1')

def exemplo(request):
    print("exemplo") # Pode fazer oque quiser dentro da função
    return HttpResponse('exemplo do app 1')