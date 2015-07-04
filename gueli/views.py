from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


#Mixin for login_required
class LoginRequiredMixin(object):

	@classmethod
	def as_view(cls):
		return login_required(super(LoginRequiredMixin, cls).as_view())


@login_required
def home(request):
	return render(request, 'homepage.html')

# Pagina de login de usuario
def login(request):

	return HttpResponseRedirect('/admin/login/')


# Mensaje de Error (GENERICO)
def mensajeError(request):
	return render(request, 'mensajeError.html')


# Mensaje de Informacion (GENERICO)
def mensajeInfo(request):
	return render(request, 'mensajeInfo.html')
