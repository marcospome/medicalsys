from django.contrib import admin
from .models import Departament
# Register your models here.
class DepartamentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'shor_name',
        'status',
    )

    search_fields = ('name',) # Barra de busqueda por nombre.
    list_filter = ('status',) # Filtro de busqueda por status.


admin.site.register(Departament, DepartamentAdmin)