# Generated by Django 3.1.1 on 2020-09-27 11:52

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer_profiles', '0002_auto_20200927_1118'),
        ('orders', '0002_auto_20200927_1952'),
        ('address', '0002_auto_20200927_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=200)),
                ('barangay', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profiles.customerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=200)),
                ('barangay', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_profiles.customerprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]