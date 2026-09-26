from django import forms
from aplication.attention.models import ServiciosAdicionales

class Servicios_adicionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = ["nombre_servicio", "costo_servicio", "descripcion", "activo"]

        error_messages = {
            "nombre_servicio": {
                "required": "El campo Nombre del Servicio es obligatorio.",
            },
            "costo_servicio": {
                "required": "El campo Costo del Servicio es obligatorio.",
                "invalid": "Ingrese un valor numérico válido para el costo.",
            },
            "descripcion": {
                "max_length": "La descripción excede el límite permitido.",
            },
            "activo": {
                "required": "Debe indicar si el servicio está activo o no.",
            },
        }

        widgets = {
            # Nombre del Servicio: campo de texto
            "nombre_servicio": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del servicio",
                }
            ),
            # Costo del Servicio: campo numérico
            "costo_servicio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el costo del servicio",
                }
            ),
            # Descripción: campo de texto largo
            "descripcion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese una descripción (opcional)",
                    "rows": 3,
                }
            ),
            # Activo: checkbox
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
