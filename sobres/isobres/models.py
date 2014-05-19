from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

def get_default_user():
	return User.objects.get(pk=1)

class Titulacio(models.Model):
	name = models.CharField (max_length=40)
	faculty = models.CharField(max_length=20)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('titulacio', kwargs={'pk':self.pk})

class Curs(models.Model):
	year = models.IntegerField(max_length=1)
	titulacio = models.ForeignKey(Titulacio)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return str(self.year)+" - "+self.titulacio.name
	def get_absolute_url(self):
		return reverse('curs' , kwargs={'pk':self.pk})


class Professor(User):
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	curs = models.ManyToManyField(Curs)
	#user = models.ForeignKey(User, unique = True)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('professor_detail', kwargs={'pk':self.pk})


class Aula(models.Model):
	name = models.CharField(max_length=20)
	capacity = models.IntegerField()
	curs = models.ForeignKey(Curs)
	user = models.ForeignKey(User, default=get_default_user)
	
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('aula', kwargs={'pk':self.pk})


	# kwargs={'idAula':self.pk}
	#def get_absolute_url(self):
	#	return reverse('Aula:Aula')

class Alumne(models.Model):
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	curs = models.ManyToManyField(Curs)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		#return "alumnesinfo/%i/" % self.id

		return reverse('alumne', kwargs={'pk':self.pk})

