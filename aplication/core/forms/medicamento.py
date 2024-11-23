from django import forms
from django.forms import ModelForm
from aplication.core.models import Medicamento

class Medicamento_Form(ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:    
        model = Medicamento
        # Campos que se muestran en este mismo orden en el formulario como etiquetas html
        fields = ["tipo", "marca_medicamento", "nombre", "descripcion", "concentracion", "cantidad", "precio", "foto", "comercial", "activo"]
     
        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "nombre": {
                "unique": "Ya existe un medicamento con este nombre",
            },
        }
     
        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario html
        widgets = {
            "tipo": forms.Select(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "marca_medicamento": forms.Select(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción del medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "concentracion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese concentración del medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese cantidad disponible",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese precio del medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "placeholder": "Suba una foto del medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "comercial": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
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