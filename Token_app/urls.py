from django.urls import path
from .views import ObtainToken

urlpatterns = [
    path('login/', ObtainToken.as_view(), name="token_obtain_pair"),
]