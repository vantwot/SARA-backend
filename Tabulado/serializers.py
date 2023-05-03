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