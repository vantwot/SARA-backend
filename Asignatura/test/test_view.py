from django.test import TestCase
from Asignatura.models import *
from Usuario.models import *
from rest_framework.reverse import reverse
from Asignatura.views import *
import json
from .data_json import define_data, error_data


class AsignaturaTestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        rol = Rol.objects.create(name="profesor",description="Empleado de la universidad")
        cls.professor = User.objects.create(username="90093825", password="user1234", first_name="Stanley", last_name="Gilbert", identification="798473733")
        cls.asignatura =  Asignatura.objects.create(code="2055510f", name="Inteligencia Artificial", credits=4, group="02", id_profesor_id=cls.professor.id)
        cls.data = json.dumps(define_data(cls.professor.id))

    def test_url(self):
        response = self.client.get("/Asignatura/")
        self.assertEqual(response.status_code, 200)

    def test_url_updateAsignatura(self):
        response = self.client.get('/Asignatura/AsignaturaUpdate/')
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        url = reverse('Asignatura:Asignatura_viewset-actualizar', args=[str(self.asignatura.id)])
        response = self.client.put(url, json.dumps({'name': 'New Name for grade'}), content_type='application/json')
        content = response.content.decode('UTF-8').replace('"', '')
        self.assertEqual(content, 'Actualización exitosa')
        self.assertEqual(response.status_code, 200)

    def test_url_ManyAsignaturas(self):
        url = reverse('Asignatura:Asignatura_viewset-many-asignaturas')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_post_ManyAsignaturas(self):
        url = reverse('Asignatura:Asignatura_viewset-many-asignaturas')
        response = self.client.post(url, self.data, content_type='application/json')
        content = response.content.decode('UTF-8').replace('"', '')
        self.assertEqual(content, 'Creación exitosa')
        self.assertEqual(response.status_code, 200)

    def test_code_grades(self):
        error_value = json.dumps(error_data(self.professor.id))
        url = reverse('Asignatura:Asignatura_viewset-many-asignaturas')
        response = self.client.post(url, error_value, content_type='application/json')
        content = json.loads(response.content.decode('UTF-8'))
        self.assertEqual(content[0],{'code': ['This field is required.']})