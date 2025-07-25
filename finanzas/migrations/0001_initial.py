# Generated by Django 5.2.4 on 2025-07-16 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('token_uri', models.CharField(max_length=255)),
                ('client_id', models.CharField(max_length=255)),
                ('client_secret', models.CharField(max_length=255)),
                ('scopes', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='inversiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('emisora_ticker', models.CharField(max_length=10)),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('cantidad_titulos', models.PositiveIntegerField()),
                ('precio_compra_titulo', models.DecimalField(decimal_places=3, max_digits=65)),
                ('costo_total_adquisicion', models.DecimalField(decimal_places=3, max_digits=65)),
                ('tipo_cambio_compra', models.DecimalField(blank=True, decimal_places=3, max_digits=65, null=True)),
                ('precio_actual_titulo', models.DecimalField(decimal_places=3, max_digits=65)),
                ('valor_actual_mercado', models.DecimalField(decimal_places=3, max_digits=65)),
                ('ganancia_perdida_no_realizada', models.DecimalField(decimal_places=3, max_digits=65)),
                ('ganancia_perdida', models.DecimalField(blank=True, decimal_places=3, max_digits=65, null=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='registro_transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=3, max_digits=65)),
                ('tipo', models.CharField(choices=[('INGRESO', 'Ingreso'), ('GASTO', 'Gasto'), ('TRANSFERENCIA', 'Transferencia')], max_length=15)),
                ('cuenta_origen', models.CharField(max_length=100)),
                ('cuenta_destino', models.CharField(max_length=100)),
                ('id_prestamo_ref', models.CharField(blank=True, max_length=10, null=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('cancelada', 'Cancelada'), ('pausada', 'Pausada'), ('pendiente', 'Pendiente de Pago')], default='pendiente', max_length=15)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('id_suscripcion_mercadopago', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='suscripcion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransaccionPendiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datos_json', models.JSONField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], default='pendiente', max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
