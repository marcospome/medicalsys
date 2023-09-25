from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.employee'
    verbose_name = 'Módulo de empleados'  # Cambia 'Nuevo Nombre' por el nombre deseado en la interfaz del administrador

