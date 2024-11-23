from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.medicamento import Medicamento_Form
from aplication.core.models import Medicamento, TipoMedicamento, MarcaMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


from django.db.models import Q

class Medicamento_ListView(LoginRequiredMixin,ListView):
    template_name = "core/medicamento/list.html"
    model = Medicamento
    context_object_name = "remedios"
    paginate_by = 4

    def get_queryset(self):
        query = Q()  # Creamos un filtro vacío
        q1 = self.request.GET.get("q")  # Obtiene el término de búsqueda del input
        if q1:
            query.add(Q(nombre__icontains=q1), Q.OR)

        # Filtrado por tipo de medicamento
        tipo = self.request.GET.get("tipo")
        if tipo and tipo != 'T':  # 'T' representa "Todos los tipos"
            query.add(Q(tipo_id=tipo), Q.AND)

        # Filtrado por marca de medicamento
        marca = self.request.GET.get("marca")
        if marca and marca != 'T':  # 'T' representa "Todas las marcas"
            query.add(Q(marca_medicamento_id=marca), Q.AND)

        # Retorna el queryset filtrado y ordenado por el nombre
        return self.model.objects.filter(query).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Medicamentos"
        context['tipos'] = TipoMedicamento.objects.all()  # Obtiene todos los tipos de medicamentos
        context['marcas'] = MarcaMedicamento.objects.all()  # Obtiene todas las marcas de medicamentos
        return context




class Medicamento_CreateView(LoginRequiredMixin,CreateView):
    model = Medicamento
    template_name = "core/medicamento/form.html"
    form_class = Medicamento_Form
    success_url = reverse_lazy('core:Medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Medicamento'
        context['grabar'] = 'Grabar Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Medicamento {form.instance.nombre}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Medicamento. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)



class Medicamento_UpdateView(LoginRequiredMixin,UpdateView):
    model = Medicamento
    template_name = "core/medicamento/form.html"
    form_class = Medicamento_Form
    success_url = reverse_lazy('core:Medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Medicamento'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Mantener la imagen existente si no se proporciona una nueva
        medicamento = form.save(commit=False)  # No guarda aún la instancia

        # Si el campo de foto está vacío, mantenemos la foto anterior
        if not form.cleaned_data['foto']:
            medicamento.foto = self.get_object().foto  # Usa la imagen existente

        medicamento.save()  # Ahora guarda la instancia

        messages.success(self.request, f"Éxito al modificar el Medicamento {medicamento.nombre}.")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtiene el objeto existente
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        


class Medicamento_DeleteView(LoginRequiredMixin,DeleteView):
    model = Medicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Medicamento_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Medicamento'
        context['description'] = f"¿Desea Eliminar el Medicamento?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    


class Medicamento_DetailView(LoginRequiredMixin,DetailView):
    model = Medicamento

    def get(self, request, *args, **kwargs):
        try:
            medicamento = self.get_object()
            # Obtener todas las especialidades
            tipo_nombre = medicamento.tipo.nombre if medicamento.tipo else 'Sin Tipo'
            marca_medicamento_nombre = medicamento.marca_medicamento.nombre if medicamento.marca_medicamento else 'Sin Marca de Medicamento'
            
            
            data = {
                'id': medicamento.id,
                'nombre': medicamento.nombre,
                'tipo': tipo_nombre,
                'marca_medicamento': marca_medicamento_nombre,
                'concentracion': medicamento.concentracion,  # Cadena de especialidades
                'cantidad': medicamento.cantidad,
                'precio': medicamento.precio,
                'foto': medicamento.get_image(),
                'comercial': medicamento.comercial,
                'activo': medicamento.activo,
            }
            return JsonResponse(data)
        except Medicamento.DoesNotExist:
            return JsonResponse({'error': 'Doctor no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Medicamento.objects.get(pk=pk)