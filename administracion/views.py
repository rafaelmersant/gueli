# VIEWS de Administracion

from django.conf import settings
from django.core.files import File
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductoSerializer, SuplidorTipoSerializer, SuplidorSerializer, \
						CategoriasProductosSerializer


from .models import Producto, Suplidor, TipoSuplidor, CategoriaProducto

import json
import datetime

# Productos Busqueda (GENERICO)
def productosSearch(request):
	return render(request, 'productos_search.html')


class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all().order_by('descripcion')
	serializer_class = ProductoSerializer


class CategoriaProductoViewSet(viewsets.ModelViewSet):
	queryset = CategoriaProducto.objects.all().order_by('descripcion')
	serializer_class = CategoriasProductosSerializer


class SuplidorTipoViewSet(viewsets.ModelViewSet):
	queryset = TipoSuplidor.objects.all()
	serializer_class = SuplidorTipoSerializer


class SuplidorViewSet(viewsets.ModelViewSet):
	queryset = Suplidor.objects.all().order_by('nombre')
	serializer_class = SuplidorSerializer


# Producto por Descripcion
class ProductoByDescrpView(APIView):

	serializer_class = ProductoSerializer

	def get(self, request, descrp=None):
		if descrp != None:
			productos = Producto.objects.filter(descripcion__contains=descrp).order_by('descripcion')
		else:
			productos = Producto.objects.all()

		response = self.serializer_class(productos, many=True)
		return Response(response.data)


# Suplidor por Nombre
class SuplidorByNombreView(APIView):

	serializer_class = SuplidorSerializer

	def get(self, request, nombre=None):
		if nombre != None:
			suplidores = Suplidor.objects.filter(nombre__contains=nombre, estatus='A').order_by('nombre')
		else:
			suplidores = Suplidor.objects.filter(estatus='A')

		response = self.serializer_class(suplidores, many=True)
		return Response(response.data)
