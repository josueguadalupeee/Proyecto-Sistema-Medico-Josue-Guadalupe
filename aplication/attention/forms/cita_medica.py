from django import forms
from aplication.attention.models import CitaMedica


class Cita_medicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ["paciente", "fecha", "hora_cita", "estado"]

        error_messages = {
            "paciente": {
                "required": "El campo Paciente es obligatorio.",
            },
            "fecha": {
                "required": "Debe seleccionar una fecha para la cita.",
            },
            "hora_cita": {
                "required": "Debe ingresar la hora de la cita.",
            },
            "estado": {
                "required": "Debe seleccionar el estado de la cita.",
            },
        }

        widgets = {
            # Paciente: se debe usar un widget Select para seleccionar el paciente
            "paciente": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione el Paciente",
                }
            ),
            # Fecha de la Cita: se usa un widget DateInput para la fecha
            "fecha": forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "placeholder": "Seleccione la Fecha",
                }
            ),
            # Hora de la Cita: se usa un widget TimeInput para la hora
            "hora_cita": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "class": "form-control",
                    "type": "time",
                    "placeholder": "Seleccione la Hora",
                }
            ),
            # Estado de la Cita: se usa un widget Select para las opciones
            "estado": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione el Estado",
                }
            ),
        }
