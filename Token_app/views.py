from .serializer import Serializador_token
from rest_framework_simplejwt.views import TokenObtainPairView

class ObtainToken(TokenObtainPairView):
    serializer_class = Serializador_token