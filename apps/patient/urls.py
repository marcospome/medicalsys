from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('success', views.SuccessView.as_view(), name='success'),
    path('alta-afiliado', views.NewUser.as_view(), name='alta de afiliados'),
]