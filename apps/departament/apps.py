from django.apps import AppConfig


class DepartamentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.departament'
    verbose_name = 'Administración Departamental'  # Cambia 'Nuevo Nombre' por el nombre deseado en la interfaz del administrador

