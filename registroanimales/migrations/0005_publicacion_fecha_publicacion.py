# Generated by Django 4.0.4 on 2022-06-23 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroanimales', '0004_alter_publicacion_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.datetime(2022, 6, 23, 13, 29, 9, 333982)),
        ),
    ]