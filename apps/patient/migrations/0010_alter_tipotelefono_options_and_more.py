# Generated by Django 4.2.6 on 2023-11-26 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_alter_certificado_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipotelefono',
            options={'verbose_name': 'Tipo de telefono', 'verbose_name_plural': 'Tipos de telefono'},
        ),
        migrations.RenameField(
            model_name='telefono',
            old_name='tipo',
            new_name='tipo_telefono',
        ),
        migrations.RemoveField(
            model_name='referente',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='referente',
            name='fecha_de_nacimiento',
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='codigo_postal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='numero',
            field=models.CharField(blank=True, default='S/N', max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cuit',
            field=models.CharField(blank=True, help_text="<span style='color: red;font-weight: bold; text-transform: uppercase;'>¡Ingresar sin caracteres especiales o espacios ( - , * , _ )!</span>", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=8, unique=True, verbose_name='Dni del afiliado'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni_foto_dorso',
            field=models.FileField(blank=True, null=True, upload_to='dni/'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni_foto_frente',
            field=models.FileField(blank=True, null=True, upload_to='dni/'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dnititular',
            field=models.CharField(blank=True, help_text="<span style='color: red;font-weight: bold; text-transform: uppercase;'>¡Colocar unicamente si el TIPO DE AFILIACIÓN ES FAMILIAR!</span>", max_length=8, null=True, verbose_name='DNI del Titular'),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='domicilio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.domicilio', verbose_name='Dirección'),
        ),
    ]
