from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.empleado import Empleado_Form
from aplication.core.models import Empleado, Cargo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q


class Empleado_ListView(LoginRequiredMixin,ListView):
    template_name = "core/empleado/list.html"
    model = Empleado
    context_object_name = "empleados"
    query = None
    paginate_by = 4

    def get_queryset(self):
    # Inicializar el query vacío
        self.query = Q()
        
        # Filtro de búsqueda por nombre o apellido
        q1 = self.request.GET.get("q")
        if q1:
            self.query.add(Q(nombres__icontains=q1) | Q(apellidos__icontains=q1), Q.OR)

        # Filtro de búsqueda por cargo
        cargo = self.request.GET.get("cargo")
        if cargo and cargo != 'T':  # Asumiendo que 'T' es para todas
            self.query.add(Q(cargo__id=cargo), Q.AND)

        # Filtro de búsqueda por estado (activo/inactivo)
        estado = self.request.GET.get("estado")
        if estado == 'A':  # Si 'A' es para activos
            self.query.add(Q(estado=True), Q.AND)
        elif estado == 'I':  # Si 'I' es para inactivos
            self.query.add(Q(estado=False), Q.AND)

        # Retornar el queryset ordenado por nombre
        return self.model.objects.filter(self.query).order_by("id")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Empleados"
        context['cargos'] = Cargo.objects.all()  # Agrega esta línea para obtener las especialidades
        return context

    
class Empleado_CreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    template_name = "core/empleado/form.html"
    form_class = Empleado_Form
    success_url = reverse_lazy('core:Empleado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Empleado'
        context['grabar'] = 'Grabar Empleado'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al crear el Empleado {form.instance.nombres}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido, simplemente se llamará a la implementación de super()
        # Esto permitirá que se mantengan los datos en el formulario al volver a cargar la página
        messages.error(self.request, "Error al crear el Empleado. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)

class Empleado_UpdateView(LoginRequiredMixin,UpdateView):
    model = Empleado
    template_name = "core/empleado/form.html"
    form_class = Empleado_Form
    success_url = reverse_lazy('core:Empleado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información del Empleado'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Empleado'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        # Mantener la imagen existente si no se proporciona una nueva
        empleado = form.save(commit=False)  # No guarda aún la instancia

        # Si el campo de foto está vacío, mantenemos la foto anterior
        if not form.cleaned_data['foto']:
            empleado.foto = self.get_object().foto  # Usa la imagen existente

        empleado.save()  # Ahora guarda la instancia

        messages.success(self.request, f"Éxito al modificar Doctor {empleado.nombres}.")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtiene el objeto existente
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class Empleado_DeleteView(LoginRequiredMixin,DeleteView):
    model = Empleado
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:Empleado_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar el Empleado'
        context['description'] = f"¿Desea Eliminar el Empleado?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    






class Empleado_DetailView(LoginRequiredMixin,DetailView):
    model = Empleado

    def get(self, request, *args, **kwargs):
        try:
            empleado = self.get_object()
            
            # Acceso directo al nombre del cargo (ForeignKey)
            cargo_nombre = empleado.cargo.nombre if empleado.cargo else 'Sin cargo'

            data = {
                'id': empleado.id,
                'nombres': empleado.nombres,
                'apellidos': empleado.apellidos,
                'sexo': empleado.sexo,
                'cedula': empleado.cedula,
                'fecha_nacimiento': empleado.fecha_nacimiento.strftime('%Y-%m-%d') if empleado.fecha_nacimiento else '',
                'cargo': cargo_nombre,
                'sueldo': empleado.sueldo,
                'direccion': empleado.direccion,
                'edad': empleado.calcular_edad(empleado.fecha_nacimiento),
                'foto': empleado.get_image(),
            }
            return JsonResponse(data)
        except Empleado.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Empleado.objects.get(pk=pk)

