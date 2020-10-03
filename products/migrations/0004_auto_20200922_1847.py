# Generated by Django 3.1.1 on 2020-09-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200922_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3),
        ),
    ]
