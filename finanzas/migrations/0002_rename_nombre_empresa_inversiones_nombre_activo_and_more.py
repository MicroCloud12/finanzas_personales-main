# Generated by Django 5.2.4 on 2025-07-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inversiones',
            old_name='nombre_empresa',
            new_name='nombre_activo',
        ),
        migrations.AddField(
            model_name='inversiones',
            name='tipo_inversion',
            field=models.CharField(choices=[('ACCION', 'Acción'), ('CRIPTO', 'Criptomoneda'), ('FONDO', 'Fondo de Inversión'), ('BONOS', 'Bonos'), ('FIBRAS', 'Fibras'), ('BIENES_RAICES', 'Bienes Raíces')], default='ACCION', max_length=30),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='cantidad_titulos',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='costo_total_adquisicion',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='emisora_ticker',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='ganancia_perdida',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='ganancia_perdida_no_realizada',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='precio_actual_titulo',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='precio_compra_titulo',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='tipo_cambio_compra',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='inversiones',
            name='valor_actual_mercado',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
