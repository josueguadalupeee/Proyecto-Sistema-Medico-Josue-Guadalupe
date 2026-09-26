from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.especialidad import Especialidad_Form
from aplication.core.models import Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class Especialidad_ListView(LoginRequiredMixin,ListView):
    template_name="core/especialidad/list.html"
    model= Especialidad
    context_object_name="especialidades"
    query=None
    paginate_by=4

    def get_queryset(self):
        self.query=Q()
        q1=self.request.GET.get("q")
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1),Q.OR)
        return self.model.objects.filter(self.query).order_by("nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Especialidades"
        return context
    
class Especialidad_CreateView(LoginRequiredMixin,CreateView):
    model= Especialidad
    template_name= "core/especialidad/form.html"
    form_class= Especialidad_Form
    success_url= reverse_lazy('core:Especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Especialidad'
        context['grabar'] = 'Grabar Especialidad'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear la Especialidad {form.instance.nombre}.")
        return response

class Especialidad_UpdateView(LoginRequiredMixin,UpdateView):
    model = Especialidad
    template_name = "core/especialidad/form.html"
    form_class = Especialidad_Form
    success_url = reverse_lazy('core:Especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Especialidad'
        context['grabar'] = 'Grabar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar la Especialidad {form.instance.nombre}.")
        return response

class Especialidad_DeleteView(LoginRequiredMixin,DeleteView):
    model = Especialidad
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Especialidad_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar la Especialidad'
        context['description'] = f"¿Desea Eliminar la Especialidad?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context