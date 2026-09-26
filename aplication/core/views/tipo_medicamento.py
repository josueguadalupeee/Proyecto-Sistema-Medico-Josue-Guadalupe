from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.tipo_medicamento import Tipo_MedicamentoForm
from aplication.core.models import TipoMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class Tipo_Medicamento_ListView(LoginRequiredMixin,ListView):
    template_name= "core/tipo_medicamento/list.html"
    model= TipoMedicamento
    context_object_name= "medicamentos"
    query=None
    paginate_by=6

    def get_queryset(self):
        self.query= Q()

        q1= self.request.GET.get("q")
        # tipo=self.request.GET.get('tipo')
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1),Q.OR)
        return self.model.objects.filter(self.query).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Tipos de medicamento"
        return context


class Tipo_Medicamento_CreateView(LoginRequiredMixin,CreateView):
    model = TipoMedicamento
    template_name = "core/tipo_medicamento/form.html"
    form_class = Tipo_MedicamentoForm
    success_url = reverse_lazy('core:Tipo_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Medicamento'
        context['grabar'] = 'Grabar Tipo de medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el tipo de Medicamento {form.instance.nombre}.")
        return response



class Tipo_Medicamento_UpdateView(LoginRequiredMixin,UpdateView):
    model = TipoMedicamento
    template_name = "core/tipo_medicamento/form.html"
    form_class = Tipo_MedicamentoForm
    success_url = reverse_lazy('core:Tipo_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Medicamento'
        context['grabar'] = 'Grabar Tipo de Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el tipo de Medicamento {form.instance.nombre}.")
        return response
    

class Tipo_Medicamento_DeleteView(LoginRequiredMixin,DeleteView):
    model = TipoMedicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Tipo_medicamento_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Tipo de Medicamento '
        context['description'] = f"¿Desea Eliminar el Tipo de Medicamento: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
class Tipo_Medicamento_DetailView(LoginRequiredMixin,DetailView):

    model= TipoMedicamento
   
    def get(self, request, *args, **kwargs):
        try:
            tipo_medic = self.get_object()
            
            data = {
                'id': tipo_medic.id,
                'nombre': tipo_medic.nombre,
                'descripcion': tipo_medic.descripcion,
                'activo': tipo_medic.activo,
            }
            return JsonResponse(data)
        except tipo_medic.DoesNotExist:
            return JsonResponse({'error': 'Tipo de medicamento no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return TipoMedicamento.objects.get(pk=pk)
    