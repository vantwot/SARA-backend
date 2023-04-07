from functools import partial
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User
from .serializers import *
import json

#View del Usuario
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #Sobrescritura del metodo create para crear el Usuario
    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        role_serializer = RoleUserSerializer(data=request.data)
        role_serializer.is_valid(raise_exception=True)
        rol = Rol.objects.filter(name=role_serializer.data['role'].lower())

        if len(rol) == 0:
            return Response({"Mesage:": "Falta agregar los roles en la tabla Rol"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        #Guarda el usuario
        user = user_serializer.save()

        #Le agrega la contraseña al usuario
        user.set_password(user_serializer.data["password"])
        user.save()

        #Asigna un rol al usuario en la tabla UserRol
        user_rol = UserRol.objects.create(id=user, id_rol=rol[0])
        user_rol.save()


        return Response({"message: ": "Se ha creado el usuario"}, status=status.HTTP_201_CREATED)


    @action(methods=['post'], detail=False, url_path='change_password')
    def change(self,request):

        new_password = PasswordSerializer(data=request.data)
        new_password.is_valid(raise_exception=True)

        user = authenticate(username=new_password.data['username'], password=new_password.data['password'])

        if user is None:
            return Response({"message:": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

        user.set_password(new_password.data['new_password'])
        user.save()

        return Response({"message:": "Se ha cambiado tu contraseña"})
    
    @action(methods=['put'], detail=True, url_path='update_user')
    def update_user(self, request, pk=None):
        user = self.get_object()
        user_serializer = self.get_serializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message:": "se han cambiado los datos"})
        
        return Response({"message:": "error en la actualozación"}, status=status.HTTP_400_BAD_REQUEST)
    
    

class RolViewset(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
