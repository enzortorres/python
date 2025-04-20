from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest, Http404
from typing import Any


# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

# Create your views here.

def blog(request):
    print("blog") # Pode fazer oque quiser dentro da função
    
    context = {
        # 'text': 'Olá blog',
        'title': 'Blog',
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'title': found_post['title'],
        'post': found_post,
    }
    
    return render(request, 'blog/post.html', context)

def exemplo(request):
    
    context = {
        'text': 'Olá exemplo do blog',
        'title': 'Exemplo',
    }
    
    return render(request, 'blog/exemplo.html', context)