from django import forms
from django.forms import ModelForm
from aplication.core.models import Paciente

class PatientForm(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            "nombres", "apellidos", "cedula", "fecha_nacimiento", "telefono", 
            "email", "sexo", "estado_civil", "direccion", "latitud", "longitud", 
            "tipo_sangre", "foto", "alergias", "enfermedades_cronicas", 
            "medicacion_actual", "cirugias_previas", "antecedentes_personales", 
            "antecedentes_familiares", "activo"
        ]
        
        error_messages = {
            "email": {"unique": "Ya existe un paciente con este email."},
            "cedula": {"unique": "Ya existe un paciente con esta cedula."},
        }

        widgets = {
            "nombres": forms.TextInput(attrs={"placeholder": "Ingrese nombres", "class": "form-control"}),
            "apellidos": forms.TextInput(attrs={"placeholder": "Ingrese apellidos", "class": "form-control"}),
            "cedula": forms.TextInput(attrs={"placeholder": "Ingrese cedula", "class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Ingrese telefono", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Ingrese correo electrónico", "class": "form-control"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "estado_civil": forms.Select(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Ingrese dirección", "class": "form-control"}),
            "latitud": forms.TextInput(attrs={"placeholder": "Coordenada: latitud", "class": "form-control"}),
            "longitud": forms.TextInput(attrs={"placeholder": "Coordenada: longitud", "class": "form-control"}),
            "tipo_sangre": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "alergias": forms.TextInput(attrs={"placeholder": "Ingrese si tiene alergias", "class": "form-control"}),
            "enfermedades_cronicas": forms.TextInput(attrs={"placeholder": "Ingrese enfermedades crónicas", "class": "form-control"}),
            "medicacion_actual": forms.TextInput(attrs={"placeholder": "Ingrese medicación actual", "class": "form-control"}),
            "cirugias_previas": forms.TextInput(attrs={"placeholder": "Ingrese cirugías previas", "class": "form-control"}),
            "antecedentes_personales": forms.TextInput(attrs={"placeholder": "Ingrese antecedentes personales", "class": "form-control"}),
            "antecedentes_familiares": forms.TextInput(attrs={"placeholder": "Ingrese antecedentes familiares", "class": "form-control"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

        labels = {
            "cedula": "Dni",
        }
# método de limpieza se ejecuta automáticamente cuando Django valida el campo nombres en el formulario al ejecutar el metodo form_valid()
# def clean_nombres(self):
#     nombres = self.cleaned_data.get("nombres")
#     # Verificar si el campo tiene menos de 1 carácter
#     if not nombres or len(nombres) < 2:
#         raise ValidationError("El nombre debe tener al menos 2 carácter.")
    
#     return nombres.upper()

# def clean_apellidos(self):
#     apellidos = self.cleaned_data.get("apellidos")
#     # Verificar si el campo tiene menos de 1 carácter
#     if not apellidos or len(apellidos) < 1:
#         raise ValidationError("El apellido debe tener al menos 1 carácter.")

#     return apellidos.upper()
