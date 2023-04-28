from django.db import models
from django.utils.timezone import now
from Usuario.models import User
from datetime import date

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


class UserTabulado(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tabulado = models.ForeignKey(Tabulado, on_delete=models.CASCADE)
    date_generated = models.DateField(default=now())

    def __str__(self):
        return f"{str(self.id_user.username)} {str(self.id_tabulado.id)}"
    
    class Meta:
        db_table = 'UserTabulado'

