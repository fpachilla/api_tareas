from rest_framework import serializers  # Importa las herramientas de Django Rest Framework (DRF) para transformar datos
from .models import Tarea               # Este serializer va a trabajar con mi modelo Tarea

# Esta clase define cómo se muestra la información de Tarea por API
class SerializadorTarea(serializers.ModelSerializer):  # Voy a crear un serializer basado en mi modelo Tarea
    class Meta:    # Meta es una clase interna de configuración. En la cual le digo al serializer con qué modelo trabaja y qué campos va a exponer
        model = Tarea                                  # Este serializer trabaja sobre el modelo Tarea
        fields = '__all__'                             # Y va a exponer todos los campos