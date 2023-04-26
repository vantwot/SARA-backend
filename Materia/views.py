from rest_framework.viewsets import ModelViewSet
from .models import Materia
from .serializers import *


#View del Usuario
class MateriaViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
