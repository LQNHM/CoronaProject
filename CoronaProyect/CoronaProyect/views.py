from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
	return render(request, "index.html")

def AutoTest(request):
	return render(request, "AutoTest.html")

def Registro(request):
	return render(request, "Registrarse.html")

def Arreglando(request):
	return	render(request, "Arreglando.html")

def Cuidados(request):
	return render(request, "Cuidados.html")