from rest_framework import serializers
from .models import *

#Serializador para los usuarios:
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class EstudianteAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteAsignatura
        fields = '__all__'