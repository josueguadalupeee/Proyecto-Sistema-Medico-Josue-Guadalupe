from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import Diagnostico


class Diagnostico_Form(ModelForm):
    class Meta:
        model=Diagnostico
        fields=["codigo","descripcion","datos_adicionales","activo"]


        error_messages={
            "codigo": {
                "unique": "Ya existe este Codigo de Diagnostico",
            },
        }

        widgets= {
            "codigo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese un codigo de Diagnostico",
                    "id": "id_diagnostico",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.TextInput(
                attrs= {
                    "placeholder": "Ingrese una Descripcion",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            ),
            "datos_adicionales": forms.TextInput(
                attrs= {
                    "placeholder": "Ingrese datos adicionales",
                    "id": "id_datos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            ),
            "activo": forms.CheckboxInput(
                attrs= {
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",

                }
            )
        }