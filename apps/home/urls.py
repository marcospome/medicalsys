from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('informacion', views.InfoView.as_view()),
    path('especialidades', views.EspecialidadesView.as_view()),

]