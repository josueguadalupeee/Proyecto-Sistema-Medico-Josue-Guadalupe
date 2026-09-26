from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import TipoMedicamento


class Tipo_MedicamentoForm(ModelForm):
    class Meta:
        model=TipoMedicamento
        fields=["nombre","descripcion","activo"]


        error_messages={
            "nombre": {
                "unique": "Ya existe este Tipo de Medicamento",
            },
        }

        widgets= {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese un Tipo de Medicamento",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs= {
                    "placeholder": "Ingrese una Descripcion",
                    "id": "id_Descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            ),
             "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }

    def clean_nombre(self):
        nombres=self.cleaned_data.get("nombre")
        if not nombres or len(nombres) < 5:
            raise ValidationError("El tipo de Medicamento debe tener al menos 5 caracter")
        
        return nombres.upper()
