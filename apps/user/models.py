from django.db import models
from apps.employee.models import Employee
from ckeditor.fields import RichTextField

# Create your models here.
class User(models.Model):
    
    #Tipo de genero.
    SEX_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('3', 'Otro')
    )


    first_name = models.CharField('Nombre', max_length=45)
    last_name = models.CharField('Apellido', max_length=40)
    birthdate = models.DateField('Fecha de nacimiento', null=True)
    phone = models.CharField('Telefono', max_length=10, blank=True, null=True)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    email = models.EmailField('Email', max_length=45, blank=True, null=True)
    dni = models.CharField('DNI',max_length=8, unique=True)
    #skill = models.ManyToManyField(Skills, verbose_name='Habilidades') # Relación Muchos a Muchos
    status = models.BooleanField('Inactivo', default=False)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Registro de pacientes'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Paciente')
    history = RichTextField('Historial')
    date = models.DateField('Fecha del historial', auto_now=True)

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales medicos'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' | Fecha del historial: ' + str(self.date)

class Shifts(models.Model):
    SHIFTS_CHOICES = (
        ('0', '8:00'),
        ('1', '8:30'),
        ('2', '9:00'),
        ('3', '10:00'),
        ('4', '11:00'),
    )

    dni = models.CharField('DNI del Paciente', max_length=8) # blank=True/null=True <- no es obligatorio llenar un campo de texto.
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    time = models.CharField('Horario', max_length=1, choices=SHIFTS_CHOICES)
    medic = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Especialista')

    


    class Meta:
        verbose_name = 'Turnos'
        verbose_name_plural = 'Registro de Turnos'