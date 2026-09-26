from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import TipoSangre


class Tipo_sangreForm(ModelForm):
    class Meta:
        model=TipoSangre
        fields=["tipo","descripcion"]


        error_messages={
            "tipo": {
                "unique": "Ya existe este tipo de sangre",
            },
        }

        widgets= {
            "tipo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese un Tipo de sangre",
                    "id": "id_Tipo de sangre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs= {
                    "placeholder": "Ingrese una Descripcion",
                    "id": "id_Descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            )
        }

def clean_tipo(self):
    tipos=self.cleaned_data.get("tipo")
    if not tipos or len(tipos) < 2:
        raise ValidationError("El tipo de sangre debe tener al menos 2 caracter")
    
    return tipos.upper()

