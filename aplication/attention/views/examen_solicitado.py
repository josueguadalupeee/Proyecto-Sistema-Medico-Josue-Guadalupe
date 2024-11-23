from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.attention.forms.examen_solicitado import Examen_solicitadoForm
from aplication.attention.models import ExamenSolicitado
from aplication.core.models import Paciente, TipoCategoria
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Examen_solicitadoListView(LoginRequiredMixin,ListView):
    template_name="attention/examen_solicitado/list.html"
    model= ExamenSolicitado
    context_object_name="examenes"
    query=None
    paginate_by=5

    def get_queryset(self):
        self.query=Q()
        q1=self.request.GET.get("q")
        if q1:
            self.query.add(Q(nombre_examen__nombre__icontains=q1),Q.OR)
        
        estado = self.request.GET.get("estado")
        if estado and estado != 'T':  # 'T' representa "Todos los tipos"
            self.query.add(Q(estado=estado), Q.AND)
        
        return self.model.objects.filter(self.query).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Citas medicas"
        context['pacientes'] = Paciente.objects.all()
        context['tiposexamen'] = TipoCategoria.objects.all()
        return context
    

class Examen_solicitadoCreateView(LoginRequiredMixin,CreateView):
    model = ExamenSolicitado
    template_name = "attention/examen_solicitado/form.html"
    form_class = Examen_solicitadoForm
    success_url = reverse_lazy('attention:Examen_solicitado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Examen'
        context['grabar'] = 'Grabar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el examen {form.instance.nombre_examen}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Examen. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)


class Examen_solicitadoUpdateView(LoginRequiredMixin,UpdateView):
    model = ExamenSolicitado
    template_name = "attention/examen_solicitado/form.html"
    form_class = Examen_solicitadoForm
    success_url = reverse_lazy('attention:Examen_solicitado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Examen'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Examen {form.instance.nombre_examen}.")
        return response
    
    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al modificar el Examen. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)
    

    
class Examen_solicitadoDeleteView(LoginRequiredMixin,DeleteView):
    model = ExamenSolicitado
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('attention:Examen_solicitado_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Examen'
        context['description'] = f"¿Desea Eliminar el Examen?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    


class Examen_solicitadoDetailView(LoginRequiredMixin,DetailView):
    model = ExamenSolicitado

    def get(self, request, *args, **kwargs):
        try:
            examen = self.get_object()
            nombre_examenes = [nombre_examen.nombre for nombre_examen in examen.nombre_examen.all()]
            nombre_examenes_str = ', '.join(nombre_examenes) if nombre_examenes else 'Sin especialidad'

            paciente_nombre = f"{examen.paciente.nombres} {examen.paciente.apellidos}" if examen.paciente else 'Sin Paciente'
            
            data = {
                'id': examen.id,
                'nombre_examen': nombre_examenes_str,
                'paciente': paciente_nombre,
                'fecha_solicitud': examen.fecha_solicitud,
                'estado': examen.estado,
            }
            return JsonResponse(data)
        except examen.DoesNotExist:
            return JsonResponse({'error': 'Horario de atencion no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return ExamenSolicitado.objects.get(pk=pk)