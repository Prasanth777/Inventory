# Generated by Django 3.0.3 on 2020-03-20 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DevApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='Image/')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('delivery', models.CharField(blank=True, max_length=10, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('client', models.CharField(blank=True, max_length=20, null=True)),
                ('ord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Order_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Image/')),
                ('ordimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DevApp.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(null=True, upload_to='Image/')),
                ('category', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('price', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Image/')),
                ('inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DevApp.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Flips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='Image/')),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('flip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DevApp.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='Flip_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Image/')),
                ('flipimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DevApp.Flips')),
            ],
        ),
    ]
