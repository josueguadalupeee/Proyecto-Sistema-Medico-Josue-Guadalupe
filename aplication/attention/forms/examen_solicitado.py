from django import forms
from aplication.attention.models import ExamenSolicitado
 # Importa las opciones para el estado del examen

class Examen_solicitadoForm(forms.ModelForm):
    class Meta:
        model = ExamenSolicitado
        fields = ["nombre_examen", "paciente", "resultado", "comentario", "estado"]

        error_messages = {
            "nombre_examen": {
                "required": "El campo Nombre del Examen es obligatorio.",
            },
            "paciente": {
                "required": "El campo Paciente es obligatorio.",
            },
            "resultado": {
                "invalid": "El archivo subido no es válido.",
            },
            "estado": {
                "required": "Debe seleccionar el estado del examen.",
            },
        }

        widgets = {
            # Nombre del Examen: campo de texto
            "nombre_examen": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del examen",
                }
            ),
            # Paciente: se debe usar un widget Select para seleccionar el paciente
            "paciente": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione el Paciente",
                }
            ),
            # Resultado: campo de archivo para subir el resultado del examen
            "resultado": forms.ClearableFileInput(
                attrs={
                    "class": "form-control-file",
                    "placeholder": "Subir resultado del examen (opcional)",
                }
            ),
            # Comentario: campo de texto largo para agregar comentarios sobre el examen
            "comentario": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese comentarios adicionales (opcional)",
                    "rows": 3,
                }
            ),
            # Estado del Examen: campo de selección con opciones predefinidas
            "estado": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Seleccione el Estado",
                }
            ),
        }
