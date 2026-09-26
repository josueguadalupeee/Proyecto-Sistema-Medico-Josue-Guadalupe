from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.marca_medicamento import Marca_MedicamentoForm
from aplication.core.models import MarcaMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class Marca_Medicamento_ListView(LoginRequiredMixin,ListView):
    template_name = "core/marca_medicamento/list.html"
    model = MarcaMedicamento
    context_object_name = "marcas"
    query = None
    paginate_by = 6

    def get_queryset(self):
        self.query = Q()

        # Obtener el parámetro de búsqueda
        q1 = self.request.GET.get("q")
        # Si se pasa un filtro de búsqueda, agregarlo al queryset
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        
        # Filtrar las marcas de medicamento y ordenarlas por el campo deseado (por ejemplo, `id` o `created_at`)
        return self.model.objects.filter(self.query).order_by('id')  # Cambia 'id' a 'created_at' si tienes este campo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Marcas"
        return context


class Marca_Medicamento_CreateView(LoginRequiredMixin,CreateView):
    model = MarcaMedicamento
    template_name = "core/marca_medicamento/form.html"
    form_class = Marca_MedicamentoForm
    success_url = reverse_lazy('core:Marca_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Marca de Medicamento'
        context['grabar'] = 'Grabar Marca de Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear la Marca tipo de Medicamento {form.instance.nombre}.")
        return response


class Marca_Medicamento_UpdateView(LoginRequiredMixin,UpdateView):
    model = MarcaMedicamento
    template_name = "core/Marca_medicamento/form.html"
    form_class = Marca_MedicamentoForm
    success_url = reverse_lazy('core:Marca_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Marca de Medicamento'
        context['grabar'] = 'Grabar la Marca de Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar la Marca de Medicamento {form.instance.nombre}.")
        return response
    

class Marca_Medicamento_DeleteView(LoginRequiredMixin,DeleteView):
    model = MarcaMedicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Marca_medicamento_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar la Marca de Medicamento '
        context['description'] = f"¿Desea Eliminar el la Marca de Medicamento: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    

class Marca_Medicamento_DetailView(LoginRequiredMixin,DetailView):

    model= MarcaMedicamento
   
    def get(self, request, *args, **kwargs):
        try:
            marca = self.get_object()
            
            data = {
                'id': marca.id,
                'nombre': marca.nombre,
                'descripcion': marca.descripcion,
                'activo': marca.activo,
            }
            return JsonResponse(data)
        except marca.DoesNotExist:
            return JsonResponse({'error': 'Marca de medicamento no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return MarcaMedicamento.objects.get(pk=pk)