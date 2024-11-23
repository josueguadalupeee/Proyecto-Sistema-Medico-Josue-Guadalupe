from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.diagnostico import Diagnostico_Form
from aplication.core.models import Diagnostico
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin




class Diagnostico_ListView(LoginRequiredMixin,ListView):
    template_name= "core/diagnostico/list.html"
    model= Diagnostico
    context_object_name="diagnosticos"
    query=None
    paginate_by=5

    def get_queryset(self):
        self.query= Q()
        q1= self.request.GET.get("q")
        # tipo=self.request.GET.get('tipo')
        if q1 is not None:
            self.query.add(Q(codigo__icontains=q1),Q.OR)
        return self.model.objects.filter(self.query).order_by("codigo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Diagnosticos"
        return context
    

class Diagnostico_CreateView(LoginRequiredMixin,CreateView):
    model = Diagnostico
    template_name = "core/diagnostico/form.html"
    form_class = Diagnostico_Form
    success_url = reverse_lazy('core:Diagnostico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Diagnostico'
        context['grabar'] = 'Grabar Diagnostico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Diagnostico{form.instance.descripcion}.")
        return response
    

class Diagnostico_UpdateView(LoginRequiredMixin,UpdateView):
    model = Diagnostico
    template_name = "core/diagnostico/form.html"
    form_class = Diagnostico_Form
    success_url = reverse_lazy('core:Diagnostico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Diagnostico'
        context['grabar'] = 'Grabar Diagnostico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Diagnostico {form.instance.descripcion}.")
        return response
    
class Diagnostico_DeleteView(LoginRequiredMixin,DeleteView):
    model = Diagnostico
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Diagnostico_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Diagnostico'
        context['description'] = f"¿Desea Eliminar el Diagnostico: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    


class Diagnostico_DetailView(LoginRequiredMixin,DetailView):
    model = Diagnostico

    def get(self, request, *args, **kwargs):
        try:
            diagnostico = self.get_object()
            
            data = {
                'id': diagnostico.id,
                'datos_adicionales': diagnostico.datos_adicionales,
            }
            return JsonResponse(data)
        except diagnostico.DoesNotExist:
            return JsonResponse({'error': 'Diagnostico no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Diagnostico.objects.get(pk=pk)