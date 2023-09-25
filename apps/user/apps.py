from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'
    verbose_name = 'Módulo de pacientes'  # Cambia 'Nuevo Nombre' por el nombre deseado en la interfaz del administrador

