# Generated by Django 4.2.6 on 2023-10-18 12:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0005_alter_user_dni2_alter_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('piso', models.CharField(blank=True, max_length=10, null=True)),
                ('entre_calles', models.CharField(blank=True, max_length=150, null=True)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('localidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=100)),
                ('dosis', models.CharField(max_length=50)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('cuit', models.CharField(blank=True, max_length=20, null=True)),
                ('apellidos', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('fecha_de_nacimiento', models.DateField()),
                ('casilla_de_mail', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Ingresa un correo válido')])),
                ('condicion_de_solicitud', models.CharField(choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')], max_length=10)),
                ('estado_de_monotributo', models.CharField(choices=[('ALTA', 'Alta'), ('EN_TRAMITE', 'En trámite')], max_length=10)),
                ('dni_foto_frente', models.FileField(upload_to='dni/')),
                ('dni_foto_dorso', models.FileField(upload_to='dni/')),
                ('certificado_de_matrimonio', models.FileField(upload_to='certificados/')),
                ('certificado_de_convivencia', models.FileField(upload_to='certificados/')),
                ('certificado_de_tutela', models.FileField(upload_to='certificados/')),
                ('credencial', models.CharField(max_length=20)),
                ('credencial_entregada', models.BooleanField(default=False)),
                ('observaciones', models.TextField()),
                ('domicilio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='PacienteTratamientoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('observaciones', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('domicilio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Referente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('fecha_de_nacimiento', models.DateField()),
                ('domicilio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.domicilio')),
                ('parroquia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.parroquia')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_telefono', models.CharField(max_length=20, unique=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='telefono',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.tipotelefono'),
        ),
        migrations.AddField(
            model_name='pacientetratamientomedico',
            name='tratamiento_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.tratamientomedico'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='referente_parroquial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.referente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsable_de_carga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefonos',
            field=models.ManyToManyField(through='patient.Telefono', to='patient.tipotelefono'),
        ),
    ]