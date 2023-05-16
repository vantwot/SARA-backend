from django.urls import path
from .views import ObtainToken,CheckToken

urlpatterns = [
    path('login/', ObtainToken.as_view(), name="token_obtain_pair"),
    path('checkToken/',CheckToken.as_view()),
]