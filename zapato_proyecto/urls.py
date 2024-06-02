"""
URL configuration for zapato_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from zapato_app import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('zapatos/', views.lista_zapatos, name='lista_zapatos'),
    path('zapatos/<int:zapato_id>/', views.zapato_detail, name='zapato_detail'),
    path('zapatos/crear/', views.crear_zapato, name='crear_zapato'),
    path('zapatos/editar/<int:zapato_id>/', views.actualizar_zapato, name='actualizar_zapato'),
    path('zapatos/eliminar/<int:zapato_id>/', views.eliminar_zapato, name='eliminar_zapato'),
    path('zapatos/hacer_pedido/<int:zapato_id>/', views.hacer_pedido, name='hacer_pedido'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('ubicaciones/', views.lista_ubicaciones, name='lista_ubicaciones'),
    path('ubicaciones/<int:ubicacion_id>/', views.detalle_ubicacion, name='detalle_ubicacion'),
    path('ubicaciones/crear/', views.crear_ubicacion, name='crear_ubicacion'),
    path('ubicaciones/editar/<int:ubicacion_id>/', views.actualizar_ubicacion, name='actualizar_ubicacion'),
    path('ubicaciones/eliminar/<int:ubicacion_id>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)