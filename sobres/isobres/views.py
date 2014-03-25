# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from isobres.models import *

def mainpage(request):
	return render_to_response(
		'mainpage.html', {
		'titlehead':'Sobres aPP',
		'pagetitle':'Welcome to the sobres application',
		'contentbody':'managing non legalfunding since 2013',
		'user':request.user
		})
	#output = template.render(variables)
	#return HttpResponse(output)

def userpage(request):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found')
	sobres = user.sobre_set_all()
	template = get_template ('userpage.html')
	variables = Context({
		'username':username,
		'sobres':sobres,

		})
	output = template.render(variables)
	return HttpResponse(output)

def titulacio(request):
	try:
		tit = Titulacio.objects.all()
		curs = Curs.objects.all()
		aula = Aula.objects.all()
		alumne = Alumne.objects.all()
		p = Professor.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('titulacio.html')
	var = Context({
		'titulacio': tit,
		'curs':curs,
		'aula':aula,
		'alumne':alumne,
		'prof':p,
		})

	output = template.render(var)
	return HttpResponse(output)