# SERIALIZERS -- Administracion

from rest_framework import serializers

from .models import Producto, Suplidor, TipoSuplidor, CategoriaProducto


# Listado de Productos
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
	unidad = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Producto
		fields = ('id','codigo','descripcion','unidad','precio','costo')
		ordering = ('descripcion',)


# Listado de Tipos de Suplidores
class SuplidorTipoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=TipoSuplidor
		fields=('descripcion',)


# Listado de Suplidores
class SuplidorSerializer(serializers.ModelSerializer):

	class Meta:
		model=Suplidor
		fields=('id','cedulaRNC','nombre', 'tipoSuplidor')


# Categorias de Productos
class CategoriasProductosSerializer(serializers.ModelSerializer):

	class Meta:
		model = CategoriaProducto
		fields = ('id', 'descripcion',)
				