from django.contrib import admin

from gueli.actions import export_as_excel

from administracion.models import Unidad, Producto, TipoSuplidor, Suplidor, CategoriaProducto

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion','nota']
	list_editable = ('descripcion', 'nota')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ['id','codigo','descripcion','unidad','precio','costo']
	list_editable = ('descripcion','unidad','precio','costo')
	search_fields = ('codigo','descripcion')

	def save_model(self, request, obj, form, change):
		obj.userLog = request.user
		obj.save()

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(TipoSuplidor)
class TipoSuplidorAdmin(admin.ModelAdmin):
	list_display = ['id','descripcion']
	list_editable = ('descripcion',)

@admin.register(Suplidor)
class SuplidorAdmin(admin.ModelAdmin):
	list_display = ['id','tipoIdentificacion','cedulaRNC','nombre','telefono','intereses','tipoSuplidor','clase']
	list_editable = ('nombre','telefono','intereses','tipoSuplidor','clase')
	search_fields = ('cedulaRNC','nombre')

	def save_model(self, request, obj, form, change):
		obj.userLog = request.user
		obj.save()