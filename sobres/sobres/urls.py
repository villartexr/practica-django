from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group 
from django.db import models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from isobres.views import *
from rest_framework import viewsets, routers
admin.autodiscover()

class AlumneViewSet(viewsets.ModelViewSet):
    model = Alumne

class TitulacioViewSet(viewsets.ModelViewSet):
    model = Titulacio

class CursViewSet(viewsets.ModelViewSet):
    model = Curs

class AulaViewSet(viewsets.ModelViewSet):

    model = Aula

class ProfessorViewSet(viewsets.ModelViewSet):
   
    model = Professor

router = routers.DefaultRouter()
router.register(r'alumnes', AlumneViewSet)
router.register(r'titulacions', TitulacioViewSet)
router.register(r'cursos', CursViewSet)
router.register(r'aules', AulaViewSet)
router.register(r'professors', ProfessorViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^sobres/', include('sobres.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^a', include(router.urls)),
    url(r'^api-restful/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^info/$', informacio),
    url(r'^aulesinfo/(\w+)/$', aula),
    url(r'^titulacionsinfo/(\w+)/$', titulacio),
    url(r'^alumnesinfo/(\w+)/$', alumne),
    url(r'^cursinfo/(\w+)/$', curs),
    url(r'^professorsinfo/(\w+)/$', professor),
    url(r'^titulacionsinfo/(\w+)/(\w+)/$', titulacio),
    url(r'^aulesinfo/(\w+)/(\w+)/$', aula),
    url(r'^alumnesinfo/(\w+)/(\w+)/$', alumne),
    url(r'^cursinfo/(\w+)/(\w+)/$', curs),
    url(r'^professorsinfo/(\w+)/(\w+)/$', professor),

)

