from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Usuario.models import *
from Asignatura.models import *
from Tabulado.models import *
from Tabulado.serializers import *
from Asignatura.serializers import AsignaturaSerializer
import json

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #Consulta el ultimo Tabulado del estudiante
        my_tabulado = UserTabulado.objects.filter(id_user=user.id).order_by('date_generated')[0]
        id_tabulado = MyTabuladoSerializer(my_tabulado)
        
        tabulado = Tabulado.objects.get(pk=id_tabulado.data['id_tabulado'])
        tabulado_srlz = TabuladoSerializer(tabulado).data

        token['username'] = user.username
        token['name'] = user.first_name
        token['last_name'] = user.last_name
        token['program'] = user.academy_program
        token['tabulado'] = tabulado_srlz

        return token