# Generated by Django 3.1.6 on 2021-04-06 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210405_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='avg_rating',
        ),
    ]
