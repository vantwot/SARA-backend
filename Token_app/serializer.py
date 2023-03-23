from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Usuario.models import *
import json

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        code = user.username
        divide = code.find("-")

        if divide !=-1:
            code = code[:divide]
            user_role = Student.objects.filter(code_student=code).values()
            token['academy_program'] = user_role[0]['academy_program']
            token['role'] = "estudiante"

        else:
            user_role = Professor.objects.filter(code_professor=code).values()
            token['faculty'] = user_role[0]['faculty']
            token['position'] = user_role[0]['position']
            token['role'] = "profesor"

        #Ahora realizo la busqueda en el modelo Usuario
        query = User.objects.get(pk=code)

        #Devuelvo los clains en el token para ser convertidos . . .

        token['code'] = query.code
        token['name'] = query.name
        token['last_name'] = query.last_name
        token['identification'] = query.identification
        token['email'] = query.email
        token['cellphone'] = query.cellphone
        token['address'] = query.address

        return token