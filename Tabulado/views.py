from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Tabulado
from .serializers import *

class Tabulado(ModelViewSet):
    queryset = Tabulado.objects.all()
    serializer_class = TabuladoSerializer
