from django.forms import ModelForm
from django import forms
from aplication.core.models import Empleado

# Definición de la clase Empleado_Form que hereda de ModelForm
class Empleado_Form(ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:
        model = Empleado
        # Campos que se muestran en este mismo orden en el formulario como etiquetas HTML
        fields = ["nombres", "apellidos","sexo", "cedula", "fecha_nacimiento", "cargo", "sueldo", "direccion", "latitud", "longitud", "foto", "activo"]

        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "cedula": {
                "unique": "Ya existe un empleado con esta cédula.",
            },
        }

        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario HTML
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_Nombres",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellidos",
                    "id": "id_Apellidos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "sexo": forms.Select(
                attrs={
                    "id": "id_sexo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "cedula": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese cédula",
                    "id": "id_Cedula",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Ingrese fecha de nacimiento",
                    "id": "id_Fecha_Nacimiento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "cargo": forms.Select(
                attrs={
                    "id": "id_Cargo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "sueldo": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese sueldo",
                    "id": "id_Sueldo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese dirección",
                    "id": "id_Direccion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "latitud": forms.TextInput(
                attrs={
                    "placeholder": "Coordenada: latitud",
                    "id": "id_Latitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "longitud": forms.TextInput(
                attrs={
                    "placeholder": "Coordenada: longitud",
                    "id": "id_Longitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "placeholder": "Seleccione una foto del empleado",
                    "id": "id_Foto",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }


        
# método de limpieza se ejecuta automáticamente cuando Django valida el campo nombres en el formulario al ejecutar el metodo form_valid()
# def clean_nombres(self):
#     nombres = self.cleaned_data.get("nombres")
#     # Verificar si el campo tiene menos de 1 carácter
#     if not nombres or len(nombres) < 2:
#         raise ValidationError("El nombre debe tener al menos 2 carácter.")
    
#     return nombres.upper()

# def clean_apellidos(self):
#     apellidos = self.cleaned_data.get("apellidos")
#     # Verificar si el campo tiene menos de 1 carácter
#     if not apellidos or len(apellidos) < 1:
#         raise ValidationError("El apellido debe tener al menos 1 carácter.")

#     return apellidos.upper()


# def clean_foto(self):
#         foto = self.cleaned_data.get('foto')
#         if foto:
#             if not foto.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#                 raise ValidationError("Solo se permiten archivos PNG o JPEG para la foto.")
#         return foto

# def clean_firmaDigital(self):
#     firmaDigital = self.cleaned_data.get('firmaDigital')
#     if firmaDigital:
#          if not firmaDigital.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             raise ValidationError("Solo se permiten archivos PNG o JPEG para la firma digital.")
#     return firmaDigital

# def clean_curriculum(self):
#     curriculum = self.cleaned_data.get('curriculum')
#     if curriculum:
#         if not curriculum.name.lower().endswith(('.pdf', '.doc', '.docx', '.jpg', '.jpeg')):
#             raise ValidationError("Solo se permiten archivos PDF, DOC, DOCX, PNG o JPEG para el curriculum.")
#     return curriculum