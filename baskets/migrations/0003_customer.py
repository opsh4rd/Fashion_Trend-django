# Generated by Django 4.2.6 on 2023-11-21 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0002_baskets_remove_cartitem_product_delete_cart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('baskets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='baskets.baskets')),
            ],
        ),
    ]