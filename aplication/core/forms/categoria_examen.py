from django import forms
from django.forms import ModelForm
from aplication.core.models import CategoriaExamen


class Categoria_examen_Form(ModelForm):
    class Meta:
        model = CategoriaExamen
        fields = ["nombre", "descripcion", "activo"]


        error_messages = {
            "nombre": {
                "unique": "Ya existe una categoría con este nombre.",
            },
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre de la categoría",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción para la categoría",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": 3,  # Para hacer el campo de texto más amplio
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

