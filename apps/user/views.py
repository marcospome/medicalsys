from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)
from .models import Shifts, User
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
class NewShiftView(CreateView):
    model = Shifts # Declaramos el modelo
    template_name = 'user/turnos.html' # Declaramos el template    #success_url = '/success'  A donde redireccionar una vez que se apreta el boton de post.
    form_class = ShiftsForm
    success_url = reverse_lazy('users_app:correcto') #Forma más eficiente de declarar URLS utilizando el paquete reverse_lazy | Declaramos un nombre más corto en urls.py
    


class SuccessView(TemplateView): #Clase del tipo TemplateView solo sirve para declarar un template.
    template_name = "employee/success.html"  # Declaramos el template


class UserListView(ListView):
    template_name = "user/lista.html"
    context_object_name = 'lista_usuarios'

    def get_queryset(self):

        return User.objects.all()
