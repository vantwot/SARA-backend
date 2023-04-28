from django.db import models
from Usuario.models import User

class Tabulado(models.Model):
    semester = models.CharField(max_length=20, blank=False)
    lost_credits = models.CharField(max_length=10, default='0')
    earned_credits = models.CharField(max_length=10, default='0')
    promedio = models.CharField(max_length=5, default='0')
    courses = models.JSONField(blank=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Tabulado'

