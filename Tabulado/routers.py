from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'Tabular', TabuladoViewSet, basename='TabuladoViewSet')

urlpatterns = router.urls
