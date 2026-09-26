from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.cargo import Cargo_Form
from aplication.core.models import Cargo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Cargo_ListView(LoginRequiredMixin,ListView):
    template_name= "core/cargo/list.html"
    model= Cargo
    context_object_name="cargos"
    query=None
    paginate_by= 5

    def get_queryset(self):
        self.query=Q()
        q1= self.request.GET.get("q")
        if q1:
            self.query.add(Q(nombre__icontains=q1),Q.OR)
        
        return self.model.objects.filter(self.query).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Cargos"
        return context
    
class Cargo_CreateView(LoginRequiredMixin,CreateView):
    model = Cargo
    template_name = "core/cargo/form.html"
    form_class = Cargo_Form
    success_url = reverse_lazy('core:Cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Cargo'
        context['grabar'] = 'Grabar Cargo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Cargo {form.instance.nombre}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Cargo. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)

class Cargo_UpdateView(LoginRequiredMixin,UpdateView):
    model = Cargo
    template_name = "core/cargo/form.html"
    form_class = Cargo_Form
    success_url = reverse_lazy('core:Cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Cargo'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Cargo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Cargo {form.instance.nombre}.")
        return response
    
    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al modificar el Cargo. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)

class Cargo_DeleteView(LoginRequiredMixin,DeleteView):
    model = Cargo
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Cargo_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Cargo'
        context['description'] = f"¿Desea Eliminar el Cargo?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    


class Cargo_DetailView(LoginRequiredMixin,DetailView):
    model = Cargo

    def get(self, request, *args, **kwargs):
        try:
            cargo = self.get_object()
            
            data = {
                'id': cargo.id,
                'nombre': cargo.nombre,
                'descripcion': cargo.descripcion,
            }
            return JsonResponse(data)
        except Cargo.DoesNotExist:
            return JsonResponse({'error': 'Cargo no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Cargo.objects.get(pk=pk)