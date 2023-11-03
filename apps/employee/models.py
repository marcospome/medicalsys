from django.db import models
from apps.departament.models import Departament
# Create your models here.
class Employee(models.Model):
    
    #Tipo de genero.
    SEX_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('3', 'Otro')
    )
    #Tipo de afiliado
    ROL_CHOICES = (
        ('0', 'Administrativo'),
        ('1', 'Medico'),
        ('3', 'Otro')
    )



    first_name = models.CharField('Nombre', max_length=45)
    last_name = models.CharField('Apellido', max_length=40)
    birthdate = models.DateField('Fecha de nacimiento', null=True)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    email = models.EmailField('Email', max_length=45, blank=True, null=True)
    dni = models.CharField('DNI',max_length=8, unique=True)
    rol = models.CharField('Rol del empleado', max_length=1, choices=ROL_CHOICES, default='3')
    area = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Área')
    status = models.BooleanField('Inactivo', default=False)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Registro de empleado'

    def __str__(self):
        return self.first_name + ' ' + self.last_name