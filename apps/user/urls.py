from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('crear-turno', views.NewShiftView.as_view(), name='turno'),
    path('success', views.SuccessView.as_view(), name='correcto'),
    path('lista-usuarios', views.UserListView.as_view(), name='lista-user'),
]