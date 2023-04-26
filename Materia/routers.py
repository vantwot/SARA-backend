from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'materia', MateriaViewSet, basename='Materia_viewset')

urlpatterns = router.urls