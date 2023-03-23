from django.contrib.auth.models import User as auth_user
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import json

#View del Usuario
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
    #Sobre-escribo el metodo create de la ViewSet
    def create(self, request, *args, **kwargs):
        
        obj_request = json.loads(request.body)
        code = ''

        serializador_user = self.get_serializer(data=request.data)
        serializador_user.is_valid(raise_exception=True)

        #Comprobación de Profesor o estudiante
        match obj_request['role'].lower():
            case "estudiante":
                #Guarda el usuario y el estudiante
                save_user = serializador_user.save()
                code = str(serializador_user.data['code']) + "-" + str(obj_request['academy_program'])

                student = Student(code_student=save_user, academy_program=obj_request['academy_program'])
                student.save()

            case "profesor":
                save_user = serializador_user.save()
                code = str(serializador_user.data['code'])

                professor = Professor(code_professor=save_user, faculty=obj_request['faculty'], position=obj_request['position'])
                professor.save()
            case _:
                return Response({"message: ": "Rol Inexistente"}, status=status.HTTP_400_BAD_REQUEST)
            
        #Creación del Usuario en el token de autenticación
        auth_user.objects.create_user(
                username=code,
                email=serializador_user.data['email'],
                password=obj_request['password'])

        return Response({"message: ": "Se ha creado todo con exito", "code": code}, status=status.HTTP_201_CREATED)