# Generated by Django 3.0.3 on 2020-02-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DevApp', '0002_auto_20200219_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
