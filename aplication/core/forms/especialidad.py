from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import Especialidad


class Especialidad_Form(ModelForm):
    class Meta:
        model=Especialidad
        fields=["nombre","descripcion","activo"]


        error_messages={
            "nombre": {
                "unique": "Ya existe esta Especialidad",
            },
        }

        widgets= {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese una Especialidad",
                    "id": "id_Nombre de la Especialidad",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs= {
                    "placeholder": "Ingrese una Descripcion",
                    "id": "id_Descripción de la Especialidad",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            )
        }

def clean_tipo(self):
    tipos=self.cleaned_data.get("nombre")
    if not tipos or len(tipos) < 5:
        raise ValidationError("La Especialidad debe tener al menos 5 caracter")
    
    return tipos.upper()