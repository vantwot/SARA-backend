from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Usuario.models import *
from Usuario.serializers import *
from Asignatura.models import *
from Asignatura.serializers import AsignaturaSerializer
from Tabulado.models import *
from Tabulado.serializers import *

import json

class Serializador_token(TokenObtainPairSerializer):

    def get_tabular(id):
        #Consulta Tabulado con Raw:
        tabulado_raw = Tabulado.objects.raw('SELECT * FROM "UserTabulado" INNER JOIN \
                                            "Tabulado" AS t ON id_tabulado_id = t.id WHERE id_user_id = %s ORDER BY t.id DESC', [id])
        if len(tabulado_raw) != 0:
            tabulado = tabulado_raw[0]
            return TabuladoSerializer(tabulado).data
        else:
            return []

    # def get_info_for_teacher(id):
    #     asignatura = []
    #     tabular = Tabulado.objects.raw('SELECT id, courses FROM "Tabulado"')
    #     for n in tabular:
    #         courses = n.courses
    #         for j in range(0, len(courses),2):
    #             asig = courses[j]
    #             if asig['id_profesor'] == id:
    #                 # query = User.objects.raw('SELECT * FROM "User" INNER JOIN \
    #                 #                             (SELECT id_user_id FROM "Tabulado" AS t INNER JOIN "UserTabulado"  AS ut ON t.id = ut.id_tabulado_id WHERE t.id = %s) \
    #                 #                             AS q ON "User".id = q.id_user_id', [n.id])
    #                 # asignatura.append({"id_profesor": asig['id_profesor'], "codigo": query[0].username, \
    #                 #                    "nombre": query[0].first_name + " " + query[0].last_name,"asignatura": asig['code'], "nota": courses[j+1]})
    #                 asignatura.append({'codigo': asig['code'], 'nombre': asig['name'], 'grupo': asig['group'], 'horario': asig['horario']})

    #     return asignatura

    def get_info_for_teacher(id):
        asignatura = []
        query = Asignatura.objects.raw('SELECT * FROM "Asignatura" WHERE id_profesor_id = %s', [id])
        for n in query:
            asignatura.append({'id': n.id,'codigo': n.code, 'nombre': n.name, 'grupo': n.group, 'horario': n.horario})

        return asignatura


    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #Consulta Rol
        rol_raw = Rol.objects.raw('SELECT * FROM "Rol" INNER JOIN "UserRol" ON id = "UserRol".id_rol_id WHERE id_id = %s', [user.id])
        rol = rol_raw[0].name

        #Consulta el ultimo Tabulado del estudiante
        # my_tabulado = UserTabulado.objects.filter(id_user=user.id).order_by('date_generated')
        # if len(my_tabulado) != 0:
        #     first_tabulado = my_tabulado[0]
        #     id_tabulado = MyTabuladoSerializer(first_tabulado)
        
        #     tabulado = Tabulado.objects.get(pk=id_tabulado.data['id_tabulado'])
        #     tabulado_srlz = TabuladoSerializer(tabulado).data
        # else:
        #     tabulado_srlz = []

        token['username'] = user.username
        token['name'] = user.first_name
        token['last_name'] = user.last_name
        token['program'] = user.academy_program
        token['role'] = rol

        if rol == 'estudiante':
            tabulado = cls.get_tabular(user.id)
            token['tabulado'] = tabulado
        else :
            token['asignaturas'] = cls.get_info_for_teacher(user.id)
            
             

        return token
    


    #Consulta el estudiante de una asignatura
    #"SELECT * FROM User AS u INNER JOIN UserTabulado AS ut ON u.id = ut.id_user_id WHERE ut.id_tabulado_id = 2"
    #SELECT * FROM User INNER JOIN (SELECT id_user_id, t.courses courses FROM Tabulado AS t INNER JOIN UserTabulado  AS ut ON t.id = ut.id_tabulado_id WHERE t.id = 3) AS q ON User.id = q.id_user_id