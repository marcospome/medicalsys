from django.shortcuts import render

# Create your views here.
from ..user.forms import *
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)
from .models import Shifts
from django.urls import reverse_lazy


# Create your views here.