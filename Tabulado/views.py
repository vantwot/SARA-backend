from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Tabulado
from .serializers import *
from Asignatura.serializers import *
from Asignatura.models import Asignatura
import json

class TabuladoViewSet(ModelViewSet):
    queryset = Tabulado.objects.all()
    serializer_class = TabuladoSerializer


    def create_courses(self, courses):
        asignatura = []

        for i in range(len(courses)):
                
                course_filter = Asignatura.objects.filter(code=courses[i][0], group=courses[i][1])[0]
                course_srlz = SimpleCourseSerializer(course_filter)
                asignatura.append(course_srlz.data)
                asignatura.append(courses[i][2])

        return asignatura
    

    def create(self, request, *args, **kwargs):
        request_obj = json.loads(request.body)
        courses = request_obj['courses']
        code = request_obj['code']
        asignatura = []


        if len(courses) != 0:
            asignatura = self.create_courses(courses)


        tabulado = self.get_serializer(data=request.data)
        if tabulado.is_valid():
            student = User.objects.filter(username=code)[0]
            tabulado.save()
            t = Tabulado.objects.get(pk=tabulado.data['id'])
            t.courses = asignatura
            t.save()

            UserTabulado.objects.create(id_user=student, id_tabulado=t)

            return Response("Se ha creado el tabulado")
        
        return Response("Este error es culpa de Geider!!!", status=status.HTTP_406_NOT_ACCEPTABLE)


    @action(methods=['post'], detail=False, url_path='AssingTabular')
    def mytabular(self,request):
        data_request = json.loads(request.body)
        student = User.objects.filter(username=data_request['code'])
        tabular = Tabulado.objects.get(pk=data_request['tabular'])

    @action(methods=['put'], detail=True, url_path='UpdateMyTabular')
    def UpdateMyTabular(self,request,pk = None):
        request_obj = json.loads(request.body)
        courses = request_obj['courses']
        asignatura = []

        if len(courses) != 0:
            asignatura = self.create_courses(courses)

        tabular = Tabulado.objects.get(pk=pk)
        tabular_serializar = self.get_serializer(tabular)

        courses = tabular_serializar.data['courses']

        for a in range(0, len(asignatura), 2):
            adicionar = True
            for i in range(0, len(courses), 2):
                if courses[i]['code'] == asignatura[a]['code']:
                    adicionar = False
            if adicionar:
                courses.append(asignatura[a])
                courses.append(asignatura[a+1])

        tabular.courses = courses

        tabular.save()

        return Response({"message": "Se ha adicionado las asignaturas al tabulado"})
    
    @action(methods=['put'], detail=True, url_path='DeleteMyTabular')
    def DeleteMyTabular(self,request,pk = None):
        request_obj = json.loads(request.body)
        asignatura = request_obj['courses']

        tabular = Tabulado.objects.get(pk=pk)
        tabular_serializar = self.get_serializer(tabular)

        courses = tabular_serializar.data['courses']
        
        longitud = len(courses)
        for a in range(0, longitud, 2):
            if a < longitud:
                if courses[a]['code'] == asignatura[0] and courses[a]['group'] == asignatura[1]:
                    courses.pop(a)
                    courses.pop(a)
                    longitud -= 2

        tabular.courses = courses

        tabular.save()

        return Response({"message": "Se ha eliminado la asignatura del tabulado"})

    @action(methods=['put'], detail=False, url_path='UpdateGrade')
    def UpdateGrade(self, request):
        request_data = UpdateGradeSerializer(data=request.data)
        request_data.is_valid(raise_exception=True)
        tabulado = Tabulado.objects.get(pk=request_data.data['id_tabulado'])
        tab_srlz = self.get_serializer(tabulado)

        courses = tabulado.courses
        for a in range(0,len(courses), 2):
            if courses[a]['id'] == int(request_data.data['code']):
                courses[a+1] = request_data.data['grade']
                break
        
        tabulado.courses = courses
        tabulado.save()

        return Response({"message": "Se ha actualizado la nota"})