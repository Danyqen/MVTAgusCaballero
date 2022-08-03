from django.db import models


class Monster(models.Model):
    nickname = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField(null=True)
    
    def __str__(self):
        return f'Monstruo {self.nickname}'