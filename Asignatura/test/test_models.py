from django.test import TestCase
from Asignatura.models import *
from Usuario.models import *
from django.utils import timezone
#from django.core.urlresolvers import reverse

# models test
class AsignaturaTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create necesary data for Asignatura
        cls.rol = Rol.objects.create(name="profesor",description="Empleado de la universidad")
        cls.professor = User.objects.create(username="90093825", password="user1234", first_name="Stanley", last_name="Gilbert", identification="798473733")
        cls.asignatura = Asignatura.objects.create(code="2055510f", name="Inteligencia Artificial", credits=4, group="02", id_profesor_id=cls.professor.id)


    def test_creation_asignatura(self):
        #Comprueba que se halla creado una instancia del modelo
        self.assertTrue(isinstance(self.asignatura, Asignatura))
        #Compara la salida de __str__ con lo esperado
        self.assertEqual(self.asignatura.__str__(), str(self.asignatura.id) + " " + str(self.asignatura.code))