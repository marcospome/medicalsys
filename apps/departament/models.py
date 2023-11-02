from django.db import models
# Create your models here.
class Departament(models.Model):
    name = models.CharField('Nombre del Departamento', max_length=50) # blank=True/null=True <- no es obligatorio llenar un campo de texto.
    shor_name = models.CharField('Nombre Corto', max_length=20, null=True, blank=True) #unique=True <- No se puede repetir el campo
    status = models.BooleanField('Inactivo', default=False)
    image = models.ImageField(null=True, upload_to= "departament")
    description = models.CharField('Descripción', max_length=150, null=True)


    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.name