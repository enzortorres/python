"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from django.http import HttpResponse

# HTTP Request <-> HTTP Response
# Django funciona por MVT (Model View Template), variação de MVC (Model View Controller)

def home(request):
    print("home") # Pode fazer oque quiser dentro da função
    return HttpResponse('Home')

def blog(request):
    print("blog") # Pode fazer oque quiser dentro da função
    return HttpResponse('Blog')

urlpatterns = [
    path('', home),
    path('blog/', blog),
    path('admin/', admin.site.urls),
]
