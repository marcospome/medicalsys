# Generated by Django 4.2.6 on 2023-10-16 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('0', 'Titular'), ('1', 'Co-Titular'), ('3', 'Familiar')], default='3', max_length=1, verbose_name='Tipo de afiliado'),
        ),
    ]