from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class IndexView (TemplateView):
    template_name='home/home.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

class InfoView (TemplateView):
    template_name='home/info.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

class EspecialidadesView (TemplateView):
    template_name='home/especialidades.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

    