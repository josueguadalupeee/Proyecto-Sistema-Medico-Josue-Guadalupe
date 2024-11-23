from datetime import datetime
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models

def validate_blood_type(value):
    valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if value not in valid_types:
        raise ValidationError(f"{value} no es un tipo de sangre válido.")

class BloodType(models.Model):
    blood_type = models.CharField(max_length=3, validators=[validate_blood_type], unique=True)

    def __str__(self):
        return self.blood_type
