from rest_framework import serializers
from .models import *

#Serializador para los usuarios:
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
