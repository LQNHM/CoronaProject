from django.shortcuts import render

# Create your views here.
def listar(request):
	lista = Usuario.objects.all()
	context = {"usuarios": lista, "saludo": "Hola. Como estas?", "numeros": lista2}

	return render(request, 'listar.html', context)

def Registro(request):
	if request.POST:
		post = request.POST
		nuevo_user = Usuario(post['usuario_id'], post['nombre'], post['apellido'], post['nacimiento'], post['email'], post['contrasena'], post['ciudad'], post['codigopostal'])
		nuevo_user.save()
	return render(request, "Registrarse.html")