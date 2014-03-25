from django.db import models
from django.contrib.auth.models import User
# Create your modelModels.Model.

"""class Donor(models.Model):
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name

class Sobre(models.Model):
	date = models.DateTimeField()
	amount = models.IntegerField()
	concept = models.TextField(max_length=100)
	donor = models.ForeignKey(Donor)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.donor.name+" - "+self.concept"""

class Titulacio(models.Model):
	name = models.CharField (max_length=40)
	faculty = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name

class Curs(models.Model):
	year = models.IntegerField(max_length=1)
	titulacio = models.ForeignKey(Titulacio)
	def __unicode__(self):
		return str(self.year)+" - "+self.titulacio.name

class Professor(models.Model):
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	curs = models.ManyToManyField(Curs)
	def __unicode__(self):
		return self.name

class Aula(models.Model):
	name = models.CharField(max_length=20)
	capacity = models.IntegerField()
	curs = models.ForeignKey(Curs)
	def __unicode__(self):
		return self.name

class Alumne(models.Model):
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	curs = models.ManyToManyField(Curs)
	def __unicode__(self):
		return self.name