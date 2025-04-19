from django.shortcuts import render
from blog.data import posts


# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def blog(request):
    print("blog") # Pode fazer oque quiser dentro da função
    
    context = {
        'text': 'Olá blog',
        'title': 'Blog',
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

def exemplo(request):
    
    context = {
        'text': 'Olá exemplo do blog',
        'title': 'Exemplo',
    }
    
    return render(request, 'blog/exemplo.html', context)