# Generated by Django 3.0.3 on 2020-02-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DevApp', '0003_auto_20200220_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
