from django.urls import path
from .views import hello_world, nginx_proxy_view

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('nginx/', nginx_proxy_view, name='nginx_proxy_view'),
]
