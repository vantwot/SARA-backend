from django.db import models

from Usuario.models import User

def prerequisiteDefault():
    return {"prerequisite_1": "", "prerequisite_2": "", "prerequisite_3": "", "prerequisite_4": ""}

def horarioDefault():
    return {"time": [], "date": [], "place": []}

# Create your models here.
class Asignatura(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    credits = models.IntegerField(blank=False)
    group = models.CharField(max_length=10, blank=False)
    prerequisite = models.JSONField(default=prerequisiteDefault, blank=True)
    horario = models.JSONField(default=horarioDefault, blank=True)
    id_profesor = models.ForeignKey(User, blank=True, on_delete= models.CASCADE)

    def __str__(self):
        return f"{str(self.id)} {self.code}"
    
    class Meta:
        db_table = "Asignatura"