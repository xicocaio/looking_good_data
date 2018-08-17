# Generated by Django 2.1 on 2018-08-16 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('date', models.DateTimeField(db_index=True)),
                ('subtotal', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=200)),
                ('payment_type', models.CharField(max_length=200)),
                ('shipping_cost', models.FloatField()),
                ('shipping_service', models.CharField(max_length=200)),
                ('address_city', models.CharField(max_length=100)),
                ('address_state', models.CharField(max_length=10)),
                ('utm_source_medium', models.CharField(max_length=200)),
                ('device_type', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('code_color', models.CharField(db_index=True, max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgd.Order')),
            ],
            options={
                'db_table': 'lgd_order_item',
            },
        ),
    ]
