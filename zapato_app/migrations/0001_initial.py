# Generated by Django 5.0.6 on 2024-05-08 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ubicaciones',
            },
        ),
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='zapatos/')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zapato_app.ubicacion')),
            ],
            options={
                'db_table': 'zapatos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pagado', 'PAGADO'), ('pendiente', 'PENDIENTE'), ('cancelado', 'CANCELADO')], max_length=50)),
                ('zapato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zapato_app.zapato')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
    ]
