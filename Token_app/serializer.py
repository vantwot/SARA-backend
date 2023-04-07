from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Usuario.models import *
import json

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token