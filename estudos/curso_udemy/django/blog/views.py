from django.shortcuts import render

# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def blog(request):
    print("blog") # Pode fazer oque quiser dentro da função
    return render(request, 'blog/index.html')

def exemplo(request):
    return render(request, 'blog/exemplo.html')