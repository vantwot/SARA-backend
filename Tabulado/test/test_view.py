from django.test import TestCase
from django.utils import timezone
from Asignatura.models import *
from Usuario.models import *
from Tabulado.models import *
from rest_framework.reverse import reverse
from Asignatura.views import *
import json


class AsignaturaTestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        rol = Rol.objects.create(name="profesor",description="Empleado de la universidad")
        cls.professor = User.objects.create(username="90093825", password="user1234", first_name="Stanley", last_name="Gilbert", identification="798473733")
        cls.estudiante = User.objects.create(username="1842917", password="user1234", first_name="Deiby", last_name="Rodriguez", identification="1107083358")
        cls.asignatura =  Asignatura.objects.create(code="2055510f", name="Inteligencia Artificial", credits=4, group="02", id_profesor_id=cls.professor.id)
        cls.tabulado = Tabulado.objects.create(semester="Feb 2023 - Jul 2023", lost_credits="0", earned_credits="0", promedio="0", courses=[["2055510f", "02", "0.0"], ["111023C", "08", "0.0"], ["404002C", "26", "0.0"]])
        cls.userTabulado = UserTabulado.objects.create(id_user=cls.estudiante, id_tabulado=cls.tabulado, date_generated=timezone.now())

    def test_url(self):
        response = self.client.get("/Tabular/")
        self.assertEqual(response.status_code, 200)

    def test_url_update(self):
        url = "/Tabular/" + str(self.tabulado.id) + "/"
        response = self.client.put(url, {"code": self.estudiante.username, "semester": "Feb 2023 - Ago 2023", "courses": [["2055510f", "02", "0.0"]]}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_url_post(self):
        response = self.client.post("/Tabular/", {"code": self.estudiante.username, "semester": "Feb 2023 - Jul 2023", "courses": [["2055510f", "02", "0.0"]]}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_url_add_course(self):
        url = "/Tabular/"+ str(self.tabulado.id) +"/UpdateMyTabular/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_url_remove_course(self):
        url = "/Tabular/"+ str(self.tabulado.id) +"/DeleteMyTabular/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_url_update_grade_course(self):
        url = "/Tabular/UpdateGrade/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)