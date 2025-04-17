from django.shortcuts import render

# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def home(request):
    print("home") # Pode fazer oque quiser dentro da função
    return render(request, 'home/index.html')

def exemplo(request):
    print("exemplo") # Pode fazer oque quiser dentro da função
    return render(request, 'home/exemplo.html')