# Generated by Django 3.2 on 2021-06-12 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fechaModificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='fechaModificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaModificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fechaModificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='fechaModificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]