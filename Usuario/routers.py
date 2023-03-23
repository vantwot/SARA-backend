from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='User_viewset')

urlpatterns = router.urls