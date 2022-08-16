from django.urls import path 
from .view import UsuarioAPIView
urlpatterns = [
     path('usuario/',UsuarioAPIView.as_view(), name = 'usuario_api ')
]