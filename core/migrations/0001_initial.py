# Generated by Django 3.2.3 on 2021-06-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('rutColaborador', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut del Colaborador')),
                ('image', models.ImageField(upload_to='img', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('contraseña', models.CharField(max_length=30, verbose_name='Contraseña')),
            ],
        ),
    ]
