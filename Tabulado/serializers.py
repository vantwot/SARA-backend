from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Tabulado

class TabuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabulado
        fields = '__all__'