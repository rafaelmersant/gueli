# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

import datetime


# Unidades de productos
class Unidad(models.Model):

	descripcion = models.CharField(max_length=20)
	nota = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.descripcion

	class Meta:
		verbose_name = 'Unidad'
		verbose_name_plural = 'Unidades'


# CATEGORIA para productos
class CategoriaProducto(models.Model):

	descripcion = models.CharField(max_length=25)

	def __unicode__(self):
		return '%s' % (self.descripcion)

	def save(self, *args, **kwargs):
		self.descripcion = self.descripcion.upper()

		super(CategoriaProducto, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Categoria de Producto'
		verbose_name_plural = 'Categorias de Productos'
		ordering = ('descripcion',)


# PRODUCTOS para registrarlos en la facturacion
class Producto(models.Model):
	
	codigo = models.CharField(max_length=10, editable=False, unique=True)
	descripcion = models.CharField(max_length=50)
	unidad = models.ForeignKey(Unidad)
	categoria = models.ForeignKey(CategoriaProducto, null=True)
	precio = models.DecimalField(max_digits=12, decimal_places=2)
	costo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	foto = models.ImageField(upload_to='productos', blank=True, null=True)

	userLog = models.ForeignKey(User, editable=False)
	datetimeServer = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % (self.descripcion)

	def save(self, *args, **kwargs):
		self.descripcion = self.descripcion.upper()

		sec = Producto.objects.all().count() + 1
		
		try:
			p = Producto.objects.get(id=self.id)
		except Producto.DoesNotExist:
			self.codigo = self.descripcion[:3].upper() + ('0000' + str(sec))[-4:]

		super(Producto, self).save(*args, **kwargs)

	class Meta:
		ordering = ['descripcion']
		verbose_name_plural = 'Productos'


# Tipo de suplidores
class TipoSuplidor(models.Model):
	
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return '%s' % (self.descripcion)

	class Meta:
		ordering = ['descripcion']
		verbose_name = 'Tipo de Suplidor'
		verbose_name_plural = 'Tipos de Suplidores'


# Suplidores/Proveedores registrados
class Suplidor(models.Model):
	
	tipoIdentificacion_choices = (('CE','Cedula'),('RN','RNC'))
	clase_choices = (('N','Normal'),('S','SuperCoop'))
	estatus_choices = (('A','Activo'), ('I','Inactivo'))
	sexo_choices = (('M','Masculino'),('F','Femenino'),)

	tipoIdentificacion = models.CharField("Tipo de Identificacion", max_length=2, choices=tipoIdentificacion_choices, default='C')
	cedulaRNC = models.CharField("Cedula o RNC", unique=True, max_length=25)
	nombre = models.CharField(max_length=60)
	sexo = models.CharField(max_length=1, choices=sexo_choices, default='M')
	direccion = models.TextField(blank=True)
	sector = models.CharField(max_length=40, blank=True, null=True)
	ciudad = models.CharField(max_length=40, blank=True, null=True)
	contacto = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	correo = models.CharField(max_length=40, blank=True, null=True)
	fax = models.CharField(max_length=50, blank=True, null=True)
	intereses = models.DecimalField("Intereses %", max_digits=5, decimal_places=2, blank=True, null=True, default=0)
	tipoSuplidor = models.ForeignKey(TipoSuplidor)
	clase = models.CharField(max_length=1, choices=clase_choices, default='N')
	tipoCuentaBancaria = models.CharField("Tipo Cuenta Bancaria", max_length=2, null=True, blank=True)
	cuentaBancaria = models.CharField("Cuenta Bancaria", max_length=20, null=True, blank=True)
	estatus = models.CharField(max_length=1, choices=estatus_choices, default='A')

	userLog = models.ForeignKey(User, editable=False)
	datetimeServer = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % (self.nombre)

	def save(self, *args, **kwargs):
		self.nombre = self.nombre.upper()

		super(Suplidor, self).save(*args, **kwargs)

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = 'Suplidores'
