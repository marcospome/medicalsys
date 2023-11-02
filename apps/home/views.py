from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from apps.departament.models import Departament

class IndexView (TemplateView):
    template_name='home/home.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

class InfoView (TemplateView):
    template_name='home/info.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

class especialiadadListView(ListView):
    template_name='home/especialidades.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!
    context_object_name = 'especialidades' # su propio nombre para la lista como variable de plantilla
    def get_queryset(self):
        # Filtramos los objetos Departament donde status es False
        return Departament.objects.filter(status=False)