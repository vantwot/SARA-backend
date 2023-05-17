from Tabulado.models import Tabulado
from rest_framework.viewsets import ModelViewSet
from .models import Asignatura
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import connection


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
    
    @action(methods=['get'], detail=True, url_path='Students')
    def student_registered(self, request, pk=None):
        students = []
        grade = 0.0
        
        json_query = '%"id": {}%'.format(pk)
        query = Tabulado.objects.raw('SELECT * FROM "User" INNER JOIN (SELECT id_user_id, courses FROM "Tabulado" AS t INNER JOIN "UserTabulado"  AS ut ON t.id = ut.id_tabulado_id WHERE courses::text LIKE %s) \
                                                AS q ON "User".id = q.id_user_id', [json_query])
        
        for a in query:
            courses = a.courses
            for j in range(0, len(courses),2):
                if courses[j]['id'] == int(pk):
                    grade = courses[j+1]
                    break

            students.append({'id': a.id,'codigo': a.username, 'nombre': a.first_name + " " + a.last_name, 'nota': grade} )
            
        return Response(students)
    
    ''' 
        * Metodo para la busqueda de las asignaturas *
    '''
    @action(methods=['get'],detail=True, url_path='Search')
    def searchSubjects(self,request, pk):
        param = '{}%'.format(pk)
        subjects = []
        query = Asignatura.objects.raw('SELECT * FROM "Asignatura" AS a INNER JOIN "User" AS u ON a.id_profesor_id = u.id WHERE a.code LIKE %s OR a.name LIKE %s', [param, param])
        for a in query:
            subjects.append({"code": a.code, "name": a.name, "credits": a.credits, "group": a.group,\
                "horario": a.horario, "professor": a.first_name + " " + a.last_name, "email": a.email})

        return Response(subjects)

class EstudianteAsignaturaViewSet(ModelViewSet):
    
    serializer_class = EstudianteAsignaturaSerializer
    queryset = EstudianteAsignaturaSerializer.Meta.model.objects.all()

    @action(methods=['GET'], detail=True, url_path='byAsignatura')
    def byAsig(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(id_asignatura=pk)
        serializer = EstudianteAsignaturaSerializer(queryset, many=True)
        return Response (serializer.data)
    
    @action(methods=['GET'], detail=True,url_path='byEstudiante')
    def byEstu(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(id_estudiante=pk)
        serializer = EstudianteAsignaturaSerializer(queryset, many=True)
        return Response (serializer.data)
