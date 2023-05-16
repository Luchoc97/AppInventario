# Generated by Django 4.2.1 on 2023-05-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoofisamInventario', '0003_alter_equipos_especificaciones_alter_equipos_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='especificaciones',
            field=models.TextField(blank=True, default='', max_length=100, null=True, verbose_name='Especificaciones'),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='fotos/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='observaciones',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='persona',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Persona'),
        ),
    ]