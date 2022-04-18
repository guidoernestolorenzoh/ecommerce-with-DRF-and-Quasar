# Generated by Django 4.0.1 on 2022-03-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_historicalproduct_image_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del Producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto'),
        ),
    ]
