from django.contrib import admin 
from django.urls import path
from . import views

app_name = 'blog'

# Django urls
# https://docs.djangoproject.com/en/5.2/topics/http/urls/

urlpatterns = [
    path('<int:id>/', views.post, name='post'), # Sempre colocar a url mais específica primeiro, para evitar problemas (quanto mais coisa na url)
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
