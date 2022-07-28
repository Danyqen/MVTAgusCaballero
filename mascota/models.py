from django.db import models

class Gato(models.Model):
    Apodo = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Soy un gato llamado Sr.{self.nombre}'   