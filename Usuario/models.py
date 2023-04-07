from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


#Sobrescritura del usuario de Django:
class User(AbstractUser):
    academy_program = models.CharField(max_length=10, blank=True)
    permission = models.CharField(max_length=150, blank=True)

    class Meta:
        db_table = "User"


class Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{str(self.id)} {self.name}"
    
    class Meta:
        db_table = "Rol"

class UserRol(models.Model):
    id = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.id)} {str(self.id_rol)}"
    
    class Meta:
        db_table = "UserRol"