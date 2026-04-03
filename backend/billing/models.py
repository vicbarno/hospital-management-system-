from django.db import models

# Create your models here.
from django.db import models
from patients.models import Patient

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='unpaid')
    