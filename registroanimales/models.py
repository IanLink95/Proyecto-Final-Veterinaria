from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#1. Base de datos "Mascotas"

class Tipoanimal(models.Model):
    id_tipoanimal= models.IntegerField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Raza(models.Model):
    id_raza= models.IntegerField(primary_key=True)
    descripcion= models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion +" "+str(self.id_raza)

class Familia(models.Model):
    id_familia= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=50)
    nombre_responsable= models.CharField(max_length=30)
    telefono= models.CharField(max_length=20)
    mail= models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
       return self.apellido+" "+ str(self.id_familia)

class Mascota(models.Model):
    id_mascota= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    peso_kg= models.DecimalField(max_digits=4,decimal_places=2)
    altura_mts= models.DecimalField(max_digits=3,decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
       return self.nombre+" "+ str(self.id_mascota)+" "+ str(self.user)


class Consulta(models.Model):
    id_consulta= models.IntegerField(primary_key=True)
    id_mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    id_familia= models.ForeignKey(Familia,on_delete=models.CASCADE)
    id_tipoanimal= models.ForeignKey(Tipoanimal,on_delete= models.CASCADE)
    id_raza= models.ForeignKey(Raza,on_delete=models.CASCADE)
    fecha_consulta=models.DateField()
    motivo_consulta=models.CharField(max_length=80)
    valor=models.DecimalField(max_digits=8,decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_consulta)+" "+str(self.id_mascota)+ " "+ str(self.user)

#2. Base de datos "Comunidad"

class Publicacion(models.Model):
    tema=models.CharField(max_length=50)
    publicacion=models.CharField(max_length=250)
    autor= models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    fecha_publicacion=models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.tema)+":"

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)

    def __str__(self):
        return str(self.user)