# Generated by Django 5.1.1 on 2024-10-05 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/foodsite_img')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/foodsite_img')),
                ('name', models.CharField(default='Enter a name', max_length=20)),
                ('description', models.CharField(default='Describe your product', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
                ('active_status', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('bio', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='images/foodsite_img')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]