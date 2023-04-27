from urllib import request
from rest_framework.viewsets import ModelViewSet
from .models import Asignatura
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response


#View del Usuario
class AsignaturaViewSet(ModelViewSet):
    
    serializer_class = AsignaturaSerializer
    queryset = AsignaturaSerializer.Meta.model.objects.all()

    @action(methods=['PUT'],detail=True,url_path='AsignaturaUpdate')
    def actualizar(self, request, pk=None):
        asignatura = self.get_object()
        asignatura_serializer = AsignaturaSerializer(asignatura, data=request.data, partial=True)
        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return Response("Actualización exitosa")
        return Response("Actualización fallida")

    @action(methods=['post'], detail=False,url_path='ManyAsignaturas')
    def many_asignaturas(self,request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response("Creación exitosa")

