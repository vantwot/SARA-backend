from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from Usuario import models
from .models import *

class TabuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabulado
        fields = '__all__'

class MyTabuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTabulado
        fields = '__all__'

class UpdateGradeSerializer(serializers.Serializer):
    id_tabulado = serializers.CharField(max_length=10, allow_null=False)
    code = serializers.CharField(max_length=20, allow_null=False)
    grade = serializers.CharField(max_length=4, allow_null=False)