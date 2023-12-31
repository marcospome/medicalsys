# Generated by Django 4.2.6 on 2023-11-27 12:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_remove_parroquia_domicilio_alter_referente_parroquia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='telefonos',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='tipo_telefono',
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.ForeignKey(default=1292332, on_delete=django.db.models.deletion.CASCADE, to='patient.telefono'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telefono',
            name='numero_de_telefono2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='calle',
            field=models.CharField(max_length=100, verbose_name='Domicilio'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='casilla_de_mail',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator(message='Ingresa un correo válido')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cuit',
            field=models.CharField(blank=True, help_text="<span style='color: red;font-weight: bold; text-transform: uppercase;'>¡Ingresar sin caracteres especiales o espacios ( - , * , _ )!</span>", max_length=20, null=True, verbose_name='CUIT'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=8, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observaciones',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='numero_de_telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='TipoTelefono',
        ),
    ]
