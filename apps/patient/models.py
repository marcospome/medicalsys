# ----------- Importaciones -----------
from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# ----------- Modelo "TIPO DE TELEFONO" -----------
class TipoTelefono(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):  
        return self.descripcion
    
# ----------- Modelo "PACIENTE" -----------
class Paciente(models.Model):
    dni = models.CharField(max_length=8)
    cuit = models.CharField(max_length=20, blank=True, null=True)  # Campo opcional
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    telefonos = models.ManyToManyField(TipoTelefono, through='Telefono')  # Cambiado 'teléfonos' a 'telefonos'
    casilla_de_mail = models.EmailField(validators=[EmailValidator(message="Ingresa un correo válido")])
    condicion_de_solicitud = models.CharField(max_length=10, choices=(('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')))
    domicilio = models.ForeignKey('Domicilio', on_delete=models.SET_NULL, blank=True, null=True)
    referente_parroquial = models.ForeignKey('Referente', on_delete=models.SET_NULL, blank=True, null=True)
    responsable_de_carga = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    estado_de_monotributo = models.CharField(max_length=10, choices=(('ALTA', 'Alta'), ('EN_TRAMITE', 'En trámite')))
    dni_foto_frente = models.FileField(upload_to='dni/')
    dni_foto_dorso = models.FileField(upload_to='dni/')
    certificado_de_matrimonio = models.FileField(upload_to='certificados/')
    certificado_de_convivencia = models.FileField(upload_to='certificados/')
    certificado_de_tutela = models.FileField(upload_to='certificados/')
    credencial = models.CharField(max_length=20)
    credencial_entregada = models.BooleanField(default=False)
    observaciones = models.TextField()

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Registro de paciente'

    # ----------- Funciones -----------
    def calcular_edad(self):
        today = timezone.now().date()
        age = today.year - self.fecha_de_nacimiento.year - ((today.month, today.day) < (self.fecha_de_nacimiento.month, self.fecha_de_nacimiento.day))
        return age

    def __str__(self):  
        return f"{self.apellidos}, {self.nombres}"

# Modelo "Domicilio"
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    piso = models.CharField(max_length=10, blank=True, null=True)
    entre_calles = models.CharField(max_length=150, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10)
    localidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Registro de Domicilio'

    # ----------- Funciones -----------
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.localidad}"

# Modelo "Referente"
class Referente(models.Model):
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, blank=True, null=True)
    parroquia = models.ForeignKey('Parroquia', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Referente Parroquial'
        verbose_name_plural = 'Registro de Referente'

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"

# Modelo "Parroquia"
class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Registro de Parroquia'

    def __str__(self):
        return self.nombre

# Modelo "TELEFONO"
class Telefono(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoTelefono, on_delete=models.CASCADE)
    numero_de_telefono = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Registro de Telefono'

    def __str__(self):
        return f"{self.tipo}, {self.numero_de_telefono}"
    
# Modelo "TRATAMIENTO MÉDICO"
class TratamientoMedico(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Tratamiento Medico'
        verbose_name_plural = 'Registro de Tratamiento'

    def __str__(self):  
        return self.descripcion

# Modelo "PACIENTE-TRATAMIENTO MEDICO"
class PacienteTratamientoMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamiento_medico = models.ForeignKey(TratamientoMedico, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    observaciones = models.TextField()

    class Meta:
        verbose_name = 'Tratamiento x Paciente'
        verbose_name_plural = 'Registro de tratamiento por paciente'

# Modelo "MEDICACIÓN"
class Medicacion(models.Model):
    medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()

    class Meta:
        verbose_name = 'Medicacion'
        verbose_name_plural = 'Registro de medicaciones'

    def __str__(self):
        return self.medicamento
