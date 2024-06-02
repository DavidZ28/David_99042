from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ubicaciones'


class Zapato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='static/imga')
    ubicacion = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'zapatos'


class Pedido(models.Model):
    zapato = models.ForeignKey(Zapato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    OPCIONES = [
        ('pagado', 'PAGADO'),
        ('pendiente', 'PENDIENTE'),
        ('cancelado', 'CANCELADO'),
    ]
    estado = models.CharField(max_length=50, choices=OPCIONES)

    def __str__(self):
        return f"Pedido de {self.zapato.nombre} - Cantidad: {self.cantidad} - Fecha: {self.fecha_pedido}"
    class Meta:
        db_table = 'pedidos'
