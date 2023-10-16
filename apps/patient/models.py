#Importaciones

from django.db import models
from ckeditor.fields import RichTextField

# ------------------ Modelo de afiliado ------------------
class User(models.Model):
    
    #Tipo de genero.
    SEX_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('3', 'Otro')
    )
    #Tipo de afiliado
    TYPE_CHOICES = (
        ('0', 'Titular'),
        ('1', 'Co-Titular'),
        ('3', 'Familiar')
    )



    first_name = models.CharField('Nombre', max_length=45)
    last_name = models.CharField('Apellido', max_length=40)
    birthdate = models.DateField('Fecha de nacimiento', null=True)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    email = models.EmailField('Email', max_length=45, blank=True, null=True)
    dni = models.CharField('DNI',max_length=8, unique=True)
    type = models.CharField('Tipo de afiliado', max_length=1, choices=TYPE_CHOICES, default='Titular')
    dni2 = models.CharField('DNI del titular',max_length=8, null=True, blank=True) # dni2: Dni del titular -> Solo es necesario si el tipo de afiliado no es Titular, por eso te permiten nulls. De esta manera se puede relacionar un grupo familiar.
    status = models.BooleanField('Inactivo', default=False)

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Registro de afiliado'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
# ------------------ Modelo de historial medico ------------------
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Afiliado')
    history = RichTextField('Historial')
    date = models.DateField('Fecha del historial', auto_now=True)

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales medicos'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' | Fecha del historial: ' + str(self.date)
    

# Modelo Telefono
