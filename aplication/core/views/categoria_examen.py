from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.categoria_examen import Categoria_examen_Form
from aplication.core.models import CategoriaExamen
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin





class Categoria_examen_ListView(LoginRequiredMixin,ListView):
    template_name= "core/categoria_examen/list.html"
    model= CategoriaExamen
    context_object_name="categorias"
    query=None
    paginate_by=5

    def get_queryset(self):
        self.query= Q()
        q1= self.request.GET.get("q")
        # tipo=self.request.GET.get('tipo')
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1),Q.OR)
        return self.model.objects.filter(self.query).order_by("nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Categorias de examen"
        return context
    


class Categoria_examen_CreateView(LoginRequiredMixin,CreateView):
    model = CategoriaExamen
    template_name = "core/categoria_examen/form.html"
    form_class = Categoria_examen_Form
    success_url = reverse_lazy('core:Categoria_examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Categoria de Examen'
        context['grabar'] = 'Grabar Categoria de Examen'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear Categoria de Examen{form.instance.nombre}.")
        return response
    


class Categoria_examen_UpdateView(LoginRequiredMixin,UpdateView):
    model = CategoriaExamen
    template_name = "core/categoria_examen/form.html"
    form_class = Categoria_examen_Form
    success_url = reverse_lazy('core:Categoria_examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Categoria de Examen'
        context['grabar'] = 'Grabar Categoria de Examen'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar la Categoria de Examen {form.instance.nombre}.")
        return response
    


class Categoria_examen_DeleteView(LoginRequiredMixin,DeleteView):
    model = CategoriaExamen
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Categoria_examen_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar la Categoria de Examen'
        context['description'] = f"¿Desea Eliminar la Categoria de Examen: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    

class Categoria_examen_DetailView(LoginRequiredMixin,DetailView):
    model = CategoriaExamen

    def get(self, request, *args, **kwargs):
        try:
            categorias = self.get_object()
            
            data = {
                'id': categorias.id,
                'nombre': categorias.nombre,
                'descripcion': categorias.descripcion,
                'activo': categorias.activo,
            }
            return JsonResponse(data)
        except categorias.DoesNotExist:
            return JsonResponse({'error': 'Categoria de Examen no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return CategoriaExamen.objects.get(pk=pk)
