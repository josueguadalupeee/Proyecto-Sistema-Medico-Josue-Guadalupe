from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.attention.forms.horario_atencion import Horario_AtencionForm
from aplication.attention.models import HorarioAtencion
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Horario_AtencionListView(LoginRequiredMixin,ListView):
    template_name="attention/horario_atencion/list.html"
    model= HorarioAtencion
    context_object_name="horarios"
    query=None
    paginate_by=6

    def get_queryset(self):
        self.query=Q()
        q1=self.request.GET.get("q")
        if q1:
            self.query.add(Q(dia_semana__icontains=q1),Q.OR)
        
        return self.model.objects.filter(self.query).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Horarios de Atencion"
        return context
    
class Horario_AtencionCreateView(LoginRequiredMixin,CreateView):
    model = HorarioAtencion
    template_name = "attention/horario_atencion/form.html"
    form_class = Horario_AtencionForm
    success_url = reverse_lazy('attention:Horario_atencion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Cargo'
        context['grabar'] = 'Grabar Horario de Atencion'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Horario de atencion {form.instance.dia_semana}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Horario de atencion. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)
    


class Horario_AtencionUpdateView(LoginRequiredMixin,UpdateView):
    model = HorarioAtencion
    template_name = "attention/horario_atencion/form.html"
    form_class = Horario_AtencionForm
    success_url = reverse_lazy('attention:Horario_atencion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Horario de atencion'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Horario de Atencion'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Horario de Atencion {form.instance.dia_semana}.")
        return response
    
    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al modificar el Horario de Atencion. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)


class Horario_AtencionDeleteView(LoginRequiredMixin,DeleteView):
    model = HorarioAtencion
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('attention:Horario_atencion_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Horario de atencion'
        context['description'] = f"¿Desea Eliminar el Horario de atencion?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context



class Horario_AtencionDetailView(LoginRequiredMixin,DetailView):
    model = HorarioAtencion

    def get(self, request, *args, **kwargs):
        try:
            horario = self.get_object()
            
            data = {
                'id': horario.id,
                'dia_semana': horario.dia_semana,
                'hora_inicio': horario.hora_inicio,
                'hora_fin': horario.hora_fin,
                'Intervalo_desde': horario.Intervalo_desde,
                'Intervalo_hasta': horario.Intervalo_hasta,
                'activo': horario.activo,
            }
            return JsonResponse(data)
        except horario.DoesNotExist:
            return JsonResponse({'error': 'Horario de atencion no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return HorarioAtencion.objects.get(pk=pk)
