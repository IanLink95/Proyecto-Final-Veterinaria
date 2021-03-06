# Generated by Django 4.0.4 on 2022-06-22 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id_familia', models.IntegerField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre_responsable', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('peso_kg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('altura_mts', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id_raza', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipoanimal',
            fields=[
                ('id_tipoanimal', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id_consulta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_consulta', models.DateField()),
                ('motivo_consulta', models.CharField(max_length=80)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroanimales.familia')),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroanimales.mascota')),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroanimales.raza')),
                ('id_tipoanimal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroanimales.tipoanimal')),
            ],
        ),
    ]
