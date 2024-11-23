from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.tipo_categoria import Tipo_Categoria_Form
from aplication.core.models import TipoCategoria,CategoriaExamen
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin




class Tipo_Categoria_ListView(LoginRequiredMixin,ListView):
    template_name= "core/tipo_categoria/list.html"
    model= TipoCategoria
    context_object_name="tipos"
    query=None
    paginate_by=5

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
        context['title1'] = "Consulta de Tipos de Categoria de Examen"
        context['categorias'] = CategoriaExamen.objects.all()
        return context
    



class Tipo_Categoria_CreateView(LoginRequiredMixin,CreateView):
    model = TipoCategoria
    template_name = "core/tipo_categoria/form.html"
    form_class = Tipo_Categoria_Form
    success_url = reverse_lazy('core:Tipo_categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Categoria de Examen'
        context['grabar'] = 'Grabar Tipo de Categoria de Examen'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear Tipo de Categoria de Examen{form.instance.nombre}.")
        return response
    


class Tipo_Categoria_UpdateView(LoginRequiredMixin,UpdateView):
    model = TipoCategoria
    template_name = "core/tipo_categoria/form.html"
    form_class = Tipo_Categoria_Form
    success_url = reverse_lazy('core:Tipo_categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Tipo de Categoria de Examen'
        context['grabar'] = 'Grabar Tipo de Categoria de Examen'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al modificar el Tipo de Categoria de Examen {form.instance.nombre}.")
        return response
    


class Tipo_Categoria_DeleteView(LoginRequiredMixin,DeleteView):
    model = TipoCategoria
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Tipo_categoria_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Tipo de Categoria de Examen'
        context['description'] = f"¿Desea Eliminar el Tipo de Categoria de Examen: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    

class Tipo_Categoria_DetailView(LoginRequiredMixin,DetailView):
    model = TipoCategoria

    def get(self, request, *args, **kwargs):
        try:
            tipo_categorias = self.get_object()

            tipo_categoria_nombre = tipo_categorias.categoria_examen.nombre if tipo_categorias.categoria_examen else 'Sin Categoria'
            
            data = {
                'id': tipo_categorias.id,
                'categoria_examen': tipo_categoria_nombre,
                'nombre': tipo_categorias.nombre,
                'descripcion': tipo_categorias.descripcion,
                'valor_minimo': tipo_categorias.valor_minimo,
                'valor_maximo': tipo_categorias.valor_maximo,
                'activo': tipo_categorias.activo,
            }
            return JsonResponse(data)
        except tipo_categorias.DoesNotExist:
            return JsonResponse({'error': 'Tipo de Categoria de Examen no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return TipoCategoria.objects.get(pk=pk)
