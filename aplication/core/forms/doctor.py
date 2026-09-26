from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import Doctor

# Definición de la clase PatientForm que hereda de ModelForm
class Doctor_Form(ModelForm):
        # Clase interna Meta para configurar el formulario
    class Meta:    
        model = Doctor
        # campos que se muestran en este mismo orden en el formulario como etiquetas html
        fields = ["nombres","apellidos","sexo","cedula","fecha_nacimiento","direccion","latitud","longitud","codigoUnicoDoctor","especialidad","telefonos","email","horario_atencion","duracion_cita","curriculum","firmaDigital","foto","imagen_receta","activo"]
     
        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "cedula": {
                "unique": "Ya existe un Doctor con esta cedula",
             },
            "email": {
                "unique": "Ya existe un Doctor con este email.",
            },
            "codigoUnicoDoctor": {
                "unique": "Ya existe un Doctor con este codigo"
            }
        }
     
        # Personalización de los widgets o etiquetas que se van a mostrar en el formulario html si no se desea el valor por default dado en el modelo
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
                    "placeholder": "Ingrese cedula",
                    "id": "id_Cedula",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type":"date",
                    "placeholder": "Ingrese feccha de nacimiento",
                    "id": "id_Fecha de Nacimiento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese direccion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "latitud": forms.TextInput(
                attrs={
                    "placeholder": "Coordenada:latitud",
                    "id": "id_latitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "longitud": forms.TextInput(
                attrs={
                    "placeholder": "Coordenada:longitud",
                    "id": "id_longitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "estado_civil": forms.Select(
                attrs={
                    "id": "id_estado_civil",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "codigoUnicoDoctor": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese codigo unico",
                    "id":"id_Código Único del Doctor",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "especialidad":  forms.SelectMultiple(
                attrs={
                    "placeholder": "Ingrese la Especialidad",
                    "id": "id_Especialidades",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "telefonos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el telefono",
                    "id": "id_Telefonos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Ingrese correo electrónico",
                    "id": "id_Correo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "horario_atencion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese los horarios de atencion",
                    "id": "id_Horario de Atencion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "duracion_cita": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese la duracion de las consultas",
                    "id": "id_Tiempo de Atencion(minutos)",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "curriculum": forms.ClearableFileInput(
                attrs={
                    "placeholder": "Ingrese el curriculum",
                    "id": "id_Curriculum",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "firmaDigital": forms.FileInput(
                attrs={
                    "placeholder": "Ingrese la firma digital",
                    "id": "id_Firma Digitall",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "placeholder": "Ingrese la foto del doctor o doctora",
                    "id": "id_Foto",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "imagen_receta": forms.FileInput(
                attrs={
                    "placeholder": "Ingrese imagen para receta",
                    "id": "id_Imagen para Recetas",
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
def clean_nombres(self):
    nombres = self.cleaned_data.get("nombres")
    # Verificar si el campo tiene menos de 1 carácter
    if not nombres or len(nombres) < 2:
        raise ValidationError("El nombre debe tener al menos 2 carácter.")
    
    return nombres.upper()

def clean_apellidos(self):
    apellidos = self.cleaned_data.get("apellidos")
    # Verificar si el campo tiene menos de 1 carácter
    if not apellidos or len(apellidos) < 1:
        raise ValidationError("El apellido debe tener al menos 1 carácter.")

    return apellidos.upper()


def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            if not foto.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Solo se permiten archivos PNG o JPEG para la foto.")
        return foto

def clean_firmaDigital(self):
    firmaDigital = self.cleaned_data.get('firmaDigital')
    if firmaDigital:
         if not firmaDigital.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise ValidationError("Solo se permiten archivos PNG o JPEG para la firma digital.")
    return firmaDigital

def clean_curriculum(self):
    curriculum = self.cleaned_data.get('curriculum')
    if curriculum:
        if not curriculum.name.lower().endswith(('.pdf', '.doc', '.docx', '.jpg', '.jpeg')):
            raise ValidationError("Solo se permiten archivos PDF, DOC, DOCX, PNG o JPEG para el curriculum.")
    return curriculum