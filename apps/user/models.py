from django.db import models

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