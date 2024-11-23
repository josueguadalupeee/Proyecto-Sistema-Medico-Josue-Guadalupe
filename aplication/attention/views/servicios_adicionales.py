from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.attention.forms.servicios_adicionales import Servicios_adicionalesForm
from aplication.attention.models import ServiciosAdicionales
from aplication.core.models import Paciente, TipoCategoria
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Servicios_adicionalesListView(LoginRequiredMixin,ListView):
    template_name = "attention/servicios_adicionales/list.html"
    model = ServiciosAdicionales
    context_object_name = "servicios"
    paginate_by = 5

    def get_queryset(self):
        # Inicializamos el filtro
        query = Q()

        # Filtro por nombre
        q1 = self.request.GET.get("q")
        if q1:
            query.add(Q(nombre_servicio__icontains=q1), Q.OR)

        # Filtro por estado activo/inactivo
        activo = self.request.GET.get("activo")
        if activo == "1":  # Activo
            query.add(Q(activo=True), Q.AND)
        elif activo == "0":  # Inactivo
            query.add(Q(activo=False), Q.AND)

        # Retornamos la lista filtrada
        return self.model.objects.filter(query).order_by("id")

    def get_context_data(self, **kwargs):
        # Añadimos títulos al contexto
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Servicios adicionales"
        # Pasamos el valor actual de los filtros para reutilizarlo en la plantilla
        context['q'] = self.request.GET.get("q", "")
        context['activo'] = self.request.GET.get("activo", "T")  # 'T' como valor predeterminado
        return context
    


class Servicios_adicionalesCreateView(LoginRequiredMixin,CreateView):
    model = ServiciosAdicionales
    template_name = "attention/servicios_adicionales/form.html"
    form_class = Servicios_adicionalesForm
    success_url = reverse_lazy('attention:Servicios_adicionales_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Servicio'
        context['grabar'] = 'Grabar Servicio'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Servicio {form.instance.nombre_servicio}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Servicio. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)
    

class Servicios_adicionalesUpdateView(LoginRequiredMixin,UpdateView):
    model = ServiciosAdicionales
    template_name = "attention/servicios_adicionales/form.html"
    form_class = Servicios_adicionalesForm
    success_url = reverse_lazy('attention:Servicios_adicionales_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Servicio'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Servicio'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Servicio {form.instance.nombre_servicio}.")
        return response
    
    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al modificar el Servicio. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)
    

class Servicios_adicionalesDeleteView(LoginRequiredMixin,DeleteView):
    model = ServiciosAdicionales
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('attention:Servicios_adicionales_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Servicio'
        context['description'] = f"¿Desea Eliminar el Servicio?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    

class Servicios_adicionalesDetailView(LoginRequiredMixin,DetailView):
    model = ServiciosAdicionales

    def get(self, request, *args, **kwargs):
        try:
            servicio = self.get_object()
           
            data = {
                'id': servicio.id,
                'nombre_servicio': servicio.nombre_servicio,
                'costo_servicio': servicio.costo_servicio,
                'descripcion': servicio.descripcion,
                'activo': servicio.activo,
            }
            return JsonResponse(data)
        except servicio.DoesNotExist:
            return JsonResponse({'error': 'Horario de atencion no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return ServiciosAdicionales.objects.get(pk=pk)

    