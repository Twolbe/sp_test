# Generated by Django 3.0.5 on 2020-11-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(max_length=10, verbose_name='banner_type'),
        ),
    ]
