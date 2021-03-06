# Generated by Django 4.0.4 on 2022-06-21 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comilon', '0008_customer_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Producto',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
