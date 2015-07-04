# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ('descripcion',),
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorias de Productos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10, editable=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.DecimalField(max_digits=12, decimal_places=2)),
                ('costo', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=b'productos', blank=True)),
                ('datetimeServer', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(to='administracion.CategoriaProducto', null=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Config 4.1) Productos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suplidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoIdentificacion', models.CharField(default=b'C', max_length=2, verbose_name=b'Tipo de Identificacion', choices=[(b'CE', b'Cedula'), (b'RN', b'RNC')])),
                ('cedulaRNC', models.CharField(unique=True, max_length=25, verbose_name=b'Cedula o RNC')),
                ('nombre', models.CharField(max_length=60)),
                ('sexo', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.TextField(blank=True)),
                ('sector', models.CharField(max_length=40, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=40, null=True, blank=True)),
                ('contacto', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=50, null=True, blank=True)),
                ('correo', models.CharField(max_length=40, null=True, blank=True)),
                ('fax', models.CharField(max_length=50, null=True, blank=True)),
                ('intereses', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name=b'Intereses %')),
                ('clase', models.CharField(default=b'N', max_length=1, choices=[(b'N', b'Normal'), (b'S', b'SuperCoop')])),
                ('tipoCuentaBancaria', models.CharField(max_length=2, null=True, verbose_name=b'Tipo Cuenta Bancaria', blank=True)),
                ('cuentaBancaria', models.CharField(max_length=20, null=True, verbose_name=b'Cuenta Bancaria', blank=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('datetimeServer', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Config 4.4) Suplidores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoSuplidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name': 'Tipo de Suplidor',
                'verbose_name_plural': 'Config 4.5) Tipos de Suplidores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=20)),
                ('nota', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='suplidor',
            name='tipoSuplidor',
            field=models.ForeignKey(to='administracion.TipoSuplidor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='suplidor',
            name='userLog',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.ForeignKey(to='administracion.Unidad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='userLog',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
