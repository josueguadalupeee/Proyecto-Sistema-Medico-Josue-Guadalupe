from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.doctor import Doctor_Form
from aplication.core.models import Doctor, Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Doctor_ListView(LoginRequiredMixin,ListView):
    template_name = "core/doctor/list.html"
    model = Doctor
    context_object_name = "doctores"
    query = None
    paginate_by = 4

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get("q")
        if q1:
            self.query.add(Q(nombres__icontains=q1) | Q(apellidos__icontains=q1), Q.OR)

        especialidad = self.request.GET.get("especialidad")
        if especialidad and especialidad != 'T':  # Asumiendo que 'T' es para todas
            self.query.add(Q(especialidad__id=especialidad), Q.AND)

        return self.model.objects.filter(self.query).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Doctores"
        context['especialidad'] = Especialidad.objects.all()  # Agrega esta línea para obtener las especialidades
        return context

    
class Doctor_CreateView(LoginRequiredMixin,CreateView):
    model = Doctor
    template_name = "core/doctor/form.html"
    form_class = Doctor_Form
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Doctor'
        context['grabar'] = 'Grabar Doctor'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Doctor {form.instance.nombres}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Doctor. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)

class Doctor_UpdateView(LoginRequiredMixin,UpdateView):
    model = Doctor
    template_name = "core/doctor/form.html"
    form_class = Doctor_Form
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Doctor'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Doctor'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Mantener la imagen existente si no se proporciona una nueva
        doctor = form.save(commit=False)  # No guarda aún la instancia

        # Si el campo de foto está vacío, mantenemos la foto anterior
        if not form.cleaned_data['foto']:
            doctor.foto = self.get_object().foto  # Usa la imagen existente

        doctor.save()  # Ahora guarda la instancia

        messages.success(self.request, f"Éxito al modificar Doctor {doctor.nombres}.")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtiene el objeto existente
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class Doctor_DeleteView(LoginRequiredMixin,DeleteView):
    model = Doctor
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:doctor_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Doctor'
        context['description'] = f"¿Desea Eliminar el Doctor?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    




class DoctorDetailView(LoginRequiredMixin,DetailView):
    model = Doctor

    def get(self, request, *args, **kwargs):
        try:
            doctor = self.get_object()
            # Obtener todas las especialidades
            especialidades = [especialidad.nombre for especialidad in doctor.especialidad.all()]
            especialidades_str = ', '.join(especialidades) if especialidades else 'Sin especialidad'
            
            data = {
                'id': doctor.id,
                'nombres': doctor.nombres,
                'apellidos': doctor.apellidos,
                'foto': doctor.get_image(),
                'especialidad': especialidades_str,  # Cadena de especialidades
                'fecha_nacimiento': doctor.fecha_nacimiento,
                'edad': doctor.calcular_edad(doctor.fecha_nacimiento),
                'cedula': doctor.cedula,
                'telefonos': doctor.telefonos,
                'direccion': doctor.direccion,
            }
            return JsonResponse(data)
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctor no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Doctor.objects.get(pk=pk)
