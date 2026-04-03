from django.db import models

# Create your models here.

from django.db import models

# Esta clase define cómo se guarda la información de las tareas
class Tarea(models.Model):                                          # Estoy creando un modelo Tarea en Django

    # Los campos de este modelo van a ser estos:
    titulo = models.CharField(max_length=100)                       # Campo de texto corto (CharField) con un máximo de 10 caracteres
    descripcion = models.TextField()                                # Campo de texto corto (TextField)
    prioridad = models.IntegerField()                               # Campo de número entero
    estado = models.CharField(max_length=20, default='pendiente')   # Por default es pendiente si no se le agrega ningún estado
    fecha_creacion = models.DateTimeField(auto_now_add=True)        # Campo de fecha y hora con agregado automático de la fecha de creación

    def __str__(self):
        return self.titulo                                          # Cuando tengas que mostrar una tarea como texto, mostra su titulo