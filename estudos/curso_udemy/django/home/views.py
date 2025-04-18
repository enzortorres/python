from django.shortcuts import render

# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def home(request):
    print("home") # Pode fazer oque quiser dentro da função
    
    context = {
        'text': 'Olá home',
        'title': 'Home',
    }
    
    return render(request, 'home/index.html', context)

def exemplo(request):
    print("global") # Pode fazer oque quiser dentro da função
    
    context = {
        'text': 'Olá exemplo do home',
        'title': 'Exemplo home',
    }
    
    return render(request, 'home/exemplo.html', context)