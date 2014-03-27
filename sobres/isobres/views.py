# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from isobres.models import *
import json#, XMLObject
from json import JSONEncoder
from django.utils import simplejson
from django.core import serializers

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

def userpage(request, username):
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

def informacio(request):
	try:
		tit = Titulacio.objects.all()
		curs = Curs.objects.all()
		aula = Aula.objects.all()
		alumne = Alumne.objects.all()
		p = Professor.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('informacio.html')
	var = Context({
		'titulacio': tit,
		'curs':curs,
		'aula':aula,
		'alumne':alumne,
		'prof':p,
		})

	output = template.render(var)
	return HttpResponse(output)

def indexmodel (request, model):
	#print model
	try:
		objectmodel = model.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template(model+'.html')
	var = Context({
		model: objectmodel,
		})
	output = template.render(var)
	return HttpResponse(output)

def httpReturn(ficherohtml, key, value ):
	template = get_template(ficherohtml)
	var = Context({
		key: value,
		'titol': 'informacio sobre '+key,
		'capcalera': key,
		})
	output = template.render(var)
	return HttpResponse(output)


def aula (request, aula,xml=None):
	if xml is None:
		try:
			aula = Aula.objects.get(id = aula)
		except:
			raise Http404('Informacio not found')
		return httpReturn("aula.html", 'aula', aula)
	else:
		return xmlResponse(Aula)

def titulacio (request, titulacio, xml=None):
	if xml is None:
		try:
			tit = Titulacio.objects.get(name = titulacio)
		except:
			raise Http404('Informacio not found')
		return httpReturn("titulacio.html", 'titulacio', tit)		
	else:
		return xmlResponse(Titulacio)
	
def xmlResponse(model):

	XMLSerializer = serializers.get_serializer("xml")
	xml_serializer = XMLSerializer()
	xml_serializer.serialize(model.objects.all())
	data = xml_serializer.getvalue()
	f = open("xml", "w")
	print >>f, data
	print data
	f.close()
	return HttpResponse(data, content_type="isobres/html+xml")

def alumne(request, alumne, xml=None):
	if xml is None:
		try:
			alu = Alumne.objects.get(name = alumne)
		except:
			raise Http404('Informacio not found')
		return httpReturn("alumne.html", 'alumne', alu)
	else:
		return xmlResponse(Alumne)
def curs(request, curs, xml=None):
	if xml is None:
		try:
			curs = Curs.objects.get(year = curs)
		except:
			raise Http404('Informacio not found')
		return httpReturn("curs.html", 'curs', curs)
	else:
		return xmlResponse(Curs)

def professor(request, prof, xml=None):
	if xml is None:
		try:
			prof = Professor.objects.get(name = prof)
		except:
			raise Http404('Informacio not found')
		return httpReturn("professor.html", 'professor', prof)
	else: 
		return xmlResponse(Professor)