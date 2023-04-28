from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Usuario.models import *
from Asignatura.models import *
from Asignatura.serializers import AsignaturaSerializer
import json

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        asignatura = Asignatura.objects.all()
        asig_serialize = AsignaturaSerializer(asignatura[0])

        token['username'] = user.username
        token['name'] = user.first_name
        token['last_name'] = user.last_name
        token['program'] = user.academy_program
        token['asignatura'] = asig_serialize.data

        return token