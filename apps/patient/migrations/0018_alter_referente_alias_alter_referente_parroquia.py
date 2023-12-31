# Generated by Django 4.2.6 on 2023-12-02 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_alter_paciente_categoria_alter_paciente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referente',
            name='alias',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='referente',
            name='parroquia',
            field=models.ForeignKey(blank=True, default='S/N', on_delete=django.db.models.deletion.CASCADE, to='patient.parroquia'),
        ),
    ]
