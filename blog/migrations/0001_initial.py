# Generated by Django 4.2.6 on 2023-11-06 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'РљР°С‚РµРіРѕСЂРёСЋ Р±Р»РѕРіР°',
                'verbose_name_plural': 'РљР°С‚РµРіРѕСЂРёРё Р±Р»РѕРіР°',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blog_image')),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategories')),
            ],
            options={
                'verbose_name': 'РЎС‚Р°С‚СЊСЏ',
                'verbose_name_plural': 'РЎС‚Р°С‚СЊРё',
            },
        ),
    ]
