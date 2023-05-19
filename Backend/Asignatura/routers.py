from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'Asignatura', AsignaturaViewSet, basename='Asignatura_viewset')
router.register(r'EstudianteAsignatura', EstudianteAsignaturaViewSet, basename='EstudianteAsignatura_viewset')

urlpatterns = router.urls