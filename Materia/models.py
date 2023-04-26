from django.db import models

# Create your models here.
class Materia(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    credits = models.IntegerField()
    group = models.CharField(max_length=10)
    prerequisite = models.JSONField()
    horario = models.JSONField()
    note = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{str(self.id)} {self.code}"
    
    class Meta:
        db_table = "Materia"