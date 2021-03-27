# Generated by Django 3.1.6 on 2021-03-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210327_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
    ]
