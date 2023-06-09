from django.test import TestCase
from Asignatura.models import *
from Usuario.models import *
from Tabulado.models import *
from django.utils import timezone
#from django.core.urlresolvers import reverse

# models test
class TabuladoTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create necesary data for Asignatura
        rol = Rol.objects.create(name="profesor",description="Empleado de la universidad")
        cls.professor = User.objects.create(username="90093825", password="user1234", first_name="Stanley", last_name="Gilbert", identification="798473733")
        cls.estudiante = User.objects.create(username="1842917", password="user1234", first_name="Deiby", last_name="Rodriguez", identification="1107083358")
        cls.asignatura =  Asignatura.objects.create(code="2055510f", name="Inteligencia Artificial", credits=4, group="02", id_profesor_id=cls.professor.id)
        cls.tabulado = Tabulado.objects.create(semester="Feb 2023 - Jul 2023", lost_credits="0", earned_credits="0", promedio="0", courses=[["2055510f", "02", "0.0"]])
        cls.userTabulado = UserTabulado.objects.create(id_user=cls.estudiante, id_tabulado=cls.tabulado, date_generated=timezone.now())
        
    def test_creation_Tabulado(self):
        #Comprueba que se halla creado una instancia del modelo
        self.assertTrue(isinstance(self.tabulado, Tabulado))
        #Compara la salida de __str__ con lo esperado
        self.assertEqual(self.tabulado.__str__(), str(self.tabulado.id))