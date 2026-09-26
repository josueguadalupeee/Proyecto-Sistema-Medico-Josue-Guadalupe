from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.tipo_sangre import Tipo_sangreForm
from aplication.core.models import TipoSangre
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.utilss.tipo_sangre_utils import validate_blood_type
from django.contrib.auth.mixins import LoginRequiredMixin


class Tipo_sangrelistview(LoginRequiredMixin,ListView):
    template_name="core/tipo sangre/list.html"
    model= TipoSangre
    context_object_name="tipos_sangre"
    query= None
    paginate_by=6

    def get_queryset(self):
        self.query= Q()
        q1= self.request.GET.get("q")
        # tipo=self.request.GET.get('tipo')
        if q1 is not None:
            self.query.add(Q(tipo__icontains=q1),Q.OR)
        return self.model.objects.filter(self.query).order_by("tipo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Pacientes"
        return context

class Tipo_sangreCreateView(LoginRequiredMixin,CreateView):
    model = TipoSangre
    template_name = "core/tipo sangre/form.html"
    form_class = Tipo_sangreForm
    success_url = reverse_lazy('core:tipo_sangre_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Sangre'
        context['grabar'] = 'Grabar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el tipo de sangre {form.instance.tipo}.")
        return response
    
class Tipo_sangreUpdateView(LoginRequiredMixin,UpdateView):
    model = TipoSangre
    template_name = "core/tipo sangre/form.html"
    form_class = Tipo_sangreForm
    success_url = reverse_lazy('core:tipo_sangre_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Sangre'
        context['grabar'] = 'Grabar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el tipo de sangre {form.instance.tipo}.")
        return response
    
    
class Tipo_sangreDeleteView(LoginRequiredMixin,DeleteView):
    model = TipoSangre
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:tipo_sangre_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar Al Paciente'
        context['description'] = f"¿Desea Eliminar el Tipo de sangre: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    