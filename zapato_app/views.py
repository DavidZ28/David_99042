from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Zapato, Pedido, Ubicacion
from .forms import UbicacionForm, ZapatoForm, PedidoForm

# Vista de inicio
def home(request):
    
    query = request.GET.get('q')

    lista_zapatos = Zapato.objects.all()
    
    if query:
        lista_zapatos = lista_zapatos.filter(name__icontains=query)

    return render(request, 'home.html', {'lista_zapatos': lista_zapatos})

# Vista para ver los detalles de un zapato
def zapato_detail(request, zapato_id):
    zapato = get_object_or_404(Zapato, pk=zapato_id)
    
    return render(request, 'zapato_detail.html', {
        'zapato' : zapato,
    })


# Vista para hacer un pedido
def hacer_pedido(request, zapato_id):
    zapato = get_object_or_404(Zapato, pk=zapato_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.zapato = zapato
            pedido.save()
            return redirect('home')
    else:
        form = PedidoForm()
    return render(request, 'hacer_pedido.html', {'form': form, 'zapato': zapato})
#vista para crear zapatos

# #@login_required
def crear_zapato(request):
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('bien')
            return redirect('lista_zapatos')
    else:
        form = ZapatoForm()
        print("mal")
    return render(request, 'crear_zapato.html', {'form': form})

# Vista para ver la lista de pedidos
# # @login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

# Vista para ver los detalles de un pedido
# @login_required
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

# Vista para eliminar un pedido
# @login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

# Vista para listar los zapatos
# #@login_required
def lista_zapatos(request):
    
    query = request.GET.get('q')

    lista_zapatos = Zapato.objects.all()
    
    
    if query:
        lista_zapatos = lista_zapatos.filter(name__icontains=query)

    return render(request, 'lista_zapatos.html', {'lista_zapatos': lista_zapatos})

# Vista para actualizar un zapato existente
# @login_required
def actualizar_zapato(request, zapato_id):
    zapato = get_object_or_404(Zapato, pk=zapato_id)
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES, instance=zapato)
        if form.is_valid():
            form.save()
            return redirect('lista_zapatos')
    else:
        form = ZapatoForm(instance=zapato)
    return render(request, 'actualizar_zapato.html', {'form': form, 'zapato': zapato})

# Vista para eliminar un zapato
# @login_required
def eliminar_zapato(request, zapato_id):
    zapato = get_object_or_404(Zapato, pk=zapato_id)
    if request.method == 'GET':
        zapato.delete()
        return redirect('lista_zapatos')

# Vista para listar las ubicaciones
# @login_required
def lista_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'lista_ubicaciones.html', {'ubicaciones': ubicaciones})

# Vista para ver los detalles de una ubicación
# @login_required
def detalle_ubicacion(request, ubicacion_id):
    ubicacion = get_object_or_404(Ubicacion, pk=ubicacion_id)
    return render(request, 'detalle_ubicacion.html', {'ubicacion': ubicacion})

# Vista para crear una nueva ubicación
# @login_required
def crear_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ubicaciones')
    else:
        form = UbicacionForm()
    return render(request, 'crear_ubicacion.html', {'form': form})

# Vista para actualizar una ubicación existente
# @login_required
def actualizar_ubicacion(request, ubicacion_id):
    ubicacion = get_object_or_404(Ubicacion, pk=ubicacion_id)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_ubicaciones')
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'actualizar_ubicacion.html', {'form': form, 'ubicacion': ubicacion})

# Vista para eliminar una ubicación
# @login_required
def eliminar_ubicacion(request, ubicacion_id):
    ubicacion = get_object_or_404(Ubicacion, pk=ubicacion_id)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('lista_ubicaciones')
    return render(request, 'eliminar_ubicacion.html', {'ubicacion': ubicacion})
