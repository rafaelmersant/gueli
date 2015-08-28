from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

#Views

from inventario.views import InventarioView, InventarioSalidaView, AjusteInvView, TransferenciaInvView, EntradaInventarioById, \
                                ImprimirEntradaInventarioView, RPTAjusteInventarioView, RPTMovimientoArticuloView, \
                                RPTExistenciaArticuloView, ListadoAjustesInvView, AjusteInventarioById, TransferenciaInvView, \
                                ListadoTransfInvView, ListadoSalidasInvView, SalidaInventarioById, InventarioEliminarView, \
                                InventarioSalidaEliminarView, RPTConteoFisicoArticuloView, getExistenciaConteoFisicoRPT, \
                                ProcesarAjusteInvView, EntradasInvBySuplidorRangoFecha

from inventario.views import ListadoEntradasInvView, ListadoAlmacenesView, getExistenciaByProductoView, \
                                getExistenciaRPT, RPTMovimientoProductoAPIView

from facturacion.views import FacturacionView, FacturaById, ImprimirFacturaView, RPTUtilidades, RPTUtilidadesView, RPTVentasDiariasView, \
                                RPTVentasResumidoView, RPTResumenVentas, FacturaEliminarView

#ViewSets
from administracion.views import SuplidorTipoViewSet, ProductoViewSet, CategoriaProductoViewSet, SuplidorViewSet, \
                                    ProductoByDescrpView, SuplidorByNombreView

from facturacion.views import ListadoFacturasViewSet

admin.site.site_header = 'GUELI AUTOGOMAS'

router=routers.DefaultRouter()

#administracion
router.register(r'suplidor', SuplidorViewSet)
router.register(r'tipoSuplidor', SuplidorTipoViewSet)
router.register(r'categoriasProductos', CategoriaProductoViewSet)

#inventario
router.register(r'inventario', ListadoEntradasInvView)
router.register(r'inventariosalidas', ListadoSalidasInvView)
router.register(r'almacenes', ListadoAlmacenesView)
router.register(r'ajustesInventario', ListadoAjustesInvView)
router.register(r'transfAlmacenes', ListadoTransfInvView)
router.register(r'producto', ProductoViewSet)

#facturacion
router.register(r'facturas', ListadoFacturasViewSet)

urlpatterns = patterns('',
    
    url(r'^$', 'gueli.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'gueli.views.login', name='login'),
    url(r'^mensajeError/$', 'gueli.views.mensajeError', name='error'),
    url(r'^mensajeInfo/$', 'gueli.views.mensajeInfo', name='info'),

    #Administracion
    url(r'^productosSearch/$', 'administracion.views.productosSearch', name='productos_search'),

    url(r'^api/suplidor/nombre/(?P<nombre>[\w\s]+)/$', SuplidorByNombreView.as_view(), name='suplidor_by_nombre'),
    url(r'^api/producto/descripcion/(?P<descrp>[\w\s]+)/$', ProductoByDescrpView.as_view(), name='producto_by_descrp'),
    
    #Inventario
    url(r'^inventario/$', InventarioView.as_view(), name='Inventario'),
    url(r'^inventario/salida/$', InventarioSalidaView.as_view(), name='Inventario_salida'),
    url(r'^inventariojson/$', EntradaInventarioById.as_view(), name='InventarioById'),
    url(r'^inventariosalidajson/$', SalidaInventarioById.as_view(), name='Inventario_SalidaById'),
    url(r'^inventario/ajuste/$', AjusteInvView.as_view(), name='AjusteInventario'),
    url(r'^inventario/ajustejson/$', AjusteInventarioById.as_view(), name='AjusteInventarioById'),
    url(r'^inventario/transferencia/$', TransferenciaInvView.as_view(), name='TransferenciaInventario'),
    url(r'^inventario/eliminar/$', InventarioEliminarView.as_view(), name='Inventario_eliminar'),
    url(r'^inventario/salida/eliminar/$', InventarioSalidaEliminarView.as_view(), name='Inventario_salida_eliminar'),
    url(r'^inventario/procesarAjuste/$', ProcesarAjusteInvView.as_view(), name='Inventario_procesar_ajuste'),
    url(r'^api/producto/existencia/(?P<codProd>[\w\s]+)/(?P<almacen>[\d]+)/$', getExistenciaByProductoView.as_view(), name='existencia_by_producto'),
    url(r'^api/inventario/entradas/(?P<suplidor>[\d]+)/(?P<fechaInicio>[\w\-]+)/(?P<fechaFin>[\w\-]+)/$', EntradasInvBySuplidorRangoFecha.as_view(), \
                                                                                                            name='Entradas_por_suplidor_y_rangoFecha'),
    
    #Inventario#Imprimir
    url(r'^inventario/print/(?P<entrada>[\d]+)/$', ImprimirEntradaInventarioView.as_view(), name='Inventario_print'),
    #Inventario#Reportes
    url(r'^inventario/reportes/existenciaArticulo/$', RPTExistenciaArticuloView.as_view(), name='Inventario_reporte_existencia'),
    url(r'^inventario/reportes/conteoFisico/$', RPTConteoFisicoArticuloView.as_view(), name='Inventario_reporte_conteoFisico'),
    url(r'^inventario/reportes/histMovArt/$', RPTMovimientoArticuloView.as_view(), name='Inventario_reporte_historico'),
    
    url(r'^inventario/reportes/ajuste/$', RPTAjusteInventarioView.as_view(), name='Inventario_reporte_ajuste'),
    url(r'^inventario/api/reportes/existencia/$', getExistenciaRPT.as_view(), name='existencia_api'),
    url(r'^inventario/api/reportes/existencia/conteoFisico/$', getExistenciaConteoFisicoRPT.as_view(), name='existencia_conteoFisico_api'),
    url(r'^api/inventario/movimiento/(?P<codProd>[\w\s]+)/(?P<fechaInicio>[\w\-]+)/(?P<fechaFin>[\w\-]+)/(?P<almacen>[\d]+)/$', \
    			 RPTMovimientoProductoAPIView.as_view(), name='mov_producto_api'),

    #Facturacion    
    url(r'^facturajson/$', FacturaById.as_view(), name='FacturaById'),
    url(r'^facturacion/$', FacturacionView.as_view(), name='Facturacion'),
    url(r'^facturacion/eliminar/$', FacturaEliminarView.as_view(), name='Facturacion_eliminar'),
    #Factura#Imprimir
    url(r'^facturacion/print/(?P<factura>[\d]+)/$', ImprimirFacturaView.as_view(), name='factura_print'),
    #Facturacion#Reportes
    url(r'^facturacion/reportes/utilidades/$', RPTUtilidades.as_view(), name='Reporte_Utilidades'),
    url(r'^facturacion/reportes/utilidades/vista/$', RPTUtilidadesView.as_view(), name='Reporte_Utilidades_vista'),
    url(r'^facturacion/reportes/ventasDiarias/$', RPTVentasDiariasView.as_view(), name='Reporte_ventasDiarias'),
    url(r'^facturacion/reportes/ventasResumido/$', RPTVentasResumidoView.as_view(), name='Reporte_ventasResumido'),
    url(r'^facturacion/reportes/ventasResumido/json/$', RPTResumenVentas.as_view(), name='Reporte_ventasResumido_json'),
    

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
)
