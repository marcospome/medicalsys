# Generated by Django 4.2.6 on 2023-12-02 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0016_remove_paciente_estado_de_monotributo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='categoria',
            field=models.CharField(choices=[('0', 'Demanda Espontánea'), ('1', 'Socio'), ('3', 'Socio Afiliado')], default='0', max_length=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.telefono', verbose_name='Número de contacto'),
        ),
    ]