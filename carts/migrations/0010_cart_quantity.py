# Generated by Django 3.1.1 on 2020-10-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20201010_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
