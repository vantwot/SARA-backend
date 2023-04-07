from email.mime import base
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='User_viewset')
router.register(r'rol', RolViewset, basename='Rol_viewset')

urlpatterns = router.urls