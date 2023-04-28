from rest_framework import serializers
from .models import *

#Serializador para los usuarios:
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class SimpleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        exclude = ['id']
