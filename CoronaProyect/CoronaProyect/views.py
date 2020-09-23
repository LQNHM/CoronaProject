from django.http import HttpResponse
from django.shortcuts import render
from usuario.models import Usuario

def inicio(request):
	return render(request, "index.html")

def AutoTest(request):
	return render(request, "AutoTest.html")

def Arreglando(request):
	return	render(request, "Arreglando.html")

def Cuidados(request):
	return render(request, "Cuidados.html")

def Login(request):
	return render(request, "Login.html")

def Adolescente(request):
	return render(request, "Adolescente.html")
