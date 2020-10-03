# Generated by Django 3.1.1 on 2020-09-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_remove_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000000),
        ),
    ]
