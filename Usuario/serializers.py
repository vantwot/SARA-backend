from dataclasses import field, fields
from timeit import repeat
from rest_framework import serializers
from .models import *

#Serializador para los usuarios:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PasswordSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, allow_null=False)
    identification = serializers.CharField(allow_blank=False, allow_null=False)
    new_password = serializers.CharField(allow_blank=False, allow_null=False)
    repeat_password = serializers.CharField(allow_blank=False, allow_null=False)

    def validate(self, data):
        if data['new_password'] != data['repeat_password']:
            raise serializers.ValidationError({"message:": "Las contraseñas no coinciden"})
        
        return data
    

class RoleUserSerializer(serializers.Serializer):
    role = serializers.CharField(allow_null=False, allow_blank=False)

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'