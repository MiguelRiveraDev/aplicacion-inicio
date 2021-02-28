from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100, unique = True)    # UNIQUE -> IT'S NOT REPEATED THE SAME EMAIL

    def __str__(self):
        return self.nombre



