from .serializer import Serializador_token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
class ObtainToken(TokenObtainPairView):
    serializer_class = Serializador_token
SECRET_KEY = 'django-insecure-x9++46qu%ln3u4mfgo!36q4*#1-#8lqg2g8^gu@r_5+4##3yt='
'''
Check Token es la funcion a la que llama la url /checkToken para revisar un token esta valido.
En request, se espera que se mande un acces token.
Si se quiere acceder a payload, solo revisar payload, que recibe el valor de jwt.decode
'''
class CheckToken(APIView):
    def post (self,request):
        print(request)
        token = request.data['jwt']
        
        if not token:
            return Response("Token no existe")

        try:
            payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response("Token invalido, token expirado")
        except jwt.InvalidSignatureError:
            return Response("Token invalido, firma no valida")
        except:
            return Response("Token invalido")

        
        return Response("Token válido")