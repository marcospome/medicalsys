from django.contrib import admin
from .models import *

class TelefonoInline(admin.TabularInline):
    model = Telefono

class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'dni',
        'nombres',
        'apellidos',
        'calcular_edad',
        'credencial',
    )

    def calcular_edad(self, obj):
        return obj.calcular_edad()
    calcular_edad.short_description = "Edad"
    calcular_edad.admin_order_field = '-fecha_de_nacimiento'
    
    search_fields = ('apellidos',)
    
    list_filter = ['referente_parroquial', 'condicion_de_solicitud', 'credencial_entregada']

    inlines = [TelefonoInline]

class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'localidad')

class ReferenteAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres')

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero_de_telefono')

class TratamientoMedicoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class PacienteTratamientoMedicoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'tratamiento_medico', 'fecha_desde', 'fecha_hasta')

class MedicacionAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'dosis', 'fecha_desde', 'fecha_hasta')

admin.site.register(Certificado)
admin.site.register(TipoCertificado)
admin.site.register(TipoTelefono)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Domicilio, DomicilioAdmin)
admin.site.register(Referente, ReferenteAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(TratamientoMedico, TratamientoMedicoAdmin)
admin.site.register(PacienteTratamientoMedico, PacienteTratamientoMedicoAdmin)
admin.site.register(Medicacion, MedicacionAdmin)
