# Generated by Django 4.0.4 on 2022-06-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroanimales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=50)),
                ('publicacion', models.CharField(max_length=250)),
            ],
        ),
    ]
