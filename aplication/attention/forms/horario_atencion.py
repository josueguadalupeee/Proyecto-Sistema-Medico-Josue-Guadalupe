from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import HorarioAtencion

class Horario_AtencionForm(ModelForm):

    class Meta:
        model = HorarioAtencion
        fields = ["dia_semana", "hora_inicio", "hora_fin", "Intervalo_desde", "Intervalo_hasta", "activo"]

        error_messages = {
            "dia_semana": {
                "unique": "Este día ya tiene un horario registrado."
            }
        }

        widgets = {
            "dia_semana": forms.Select(
                attrs={
                    "placeholder": "Seleccione el Día de la Semana",
                    "id": "id_dia_semana",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "hora_inicio": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "placeholder": "Ingrese la Hora de Inicio",
                    "id": "id_hora_inicio",
                    "type": "time",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "hora_fin": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "placeholder": "Ingrese la Hora de Fin",
                    "id": "id_hora_fin",
                    "type": "time",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "Intervalo_desde": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "placeholder": "Ingrese el Inicio del Intervalo",
                    "id": "id_Intervalo_desde",
                    "type": "time",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "Intervalo_hasta": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "placeholder": "Ingrese el Fin del Intervalo",
                    "id": "id_Intervalo_hasta",
                    "type": "time",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
        }
