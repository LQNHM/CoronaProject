from django.urls import path
from usuario import views

urlpatterns = [
	path('listar/', views.listar),
	path('Registrarse/', views.Registro),
]