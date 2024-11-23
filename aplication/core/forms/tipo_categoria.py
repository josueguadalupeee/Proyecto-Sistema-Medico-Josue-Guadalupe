from django.forms import ModelForm
from django import forms
from aplication.core.models import TipoCategoria

class Tipo_Categoria_Form(ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:
        model = TipoCategoria
        # Campos que se mostrarán en el formulario según el modelo y en el mismo orden
        fields = [
            "categoria_examen", "nombre", "descripcion", 
            "valor_minimo", "valor_maximo", "activo"
        ]

        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "categoria_examen": {
                "required": "Debe seleccionar una categoría de examen.",
            },
            "nombre": {
                "required": "El nombre del examen es obligatorio.",
            },
        }

        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario HTML
        widgets = {
            "categoria_examen": forms.Select(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre del examen",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción del examen (opcional)",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": "4",
                }
            ),
            "valor_minimo": forms.TextInput(
                attrs={
                    "placeholder": "Valor mínimo de referencia",
                    "id": "id_valor_minimo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "valor_maximo": forms.TextInput(
                attrs={
                    "placeholder": "Valor máximo de referencia",
                    "id": "id_valor_maximo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }
