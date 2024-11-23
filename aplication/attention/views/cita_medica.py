from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.attention.forms.cita_medica import Cita_medicaForm
from aplication.attention.models import CitaMedica
from aplication.core.models import Paciente
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

from django.views.generic import ListView
from django.db.models import Q

from doctor import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


class Cita_medicaListView(LoginRequiredMixin,ListView):
    template_name="attention/cita_medica/list.html"
    model= CitaMedica
    context_object_name="citas"
    query=None
    paginate_by=5

    def get_queryset(self):
        self.query=Q()
        q1=self.request.GET.get("q")
        if q1:
            self.query.add(Q(paciente__cedula__iexact=q1),Q.OR)
        
        estado = self.request.GET.get("estado")
        if estado and estado != 'T':  # 'T' representa "Todos los tipos"
            self.query.add(Q(estado=estado), Q.AND)
        
        return self.model.objects.filter(self.query).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Citas medicas"
        context['pacientes'] = Paciente.objects.all()
        return context
    

class Cita_medicaCreateView(LoginRequiredMixin,CreateView):
    model = CitaMedica
    template_name = "attention/cita_medica/form.html"
    form_class = Cita_medicaForm
    success_url = reverse_lazy('attention:Cita_medica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de la Cita Medica'
        context['grabar'] = 'Grabar Cita medica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        cita = form.instance  # La cita recién creada
        paciente = cita.paciente  # El paciente asociado
        
        # Enviar correo al paciente
        if paciente.email:  # Asegúrate de que el paciente tiene un email registrado
            try:
                send_mail(
                    subject=f'Confirmación de Cita Médica - {paciente.nombres} {paciente.apellidos}',
                    message=(
                        f'Estimado/a {paciente.nombres} {paciente.apellidos},\n\n'
                        f'Su cita médica ha sido registrada con éxito.\n\n'
                        f'Detalles de la cita:\n'
                        f'- Fecha: {cita.fecha}\n'
                        f'- Hora: {cita.hora_cita}\n'
                        f'- Estado: {cita.estado}\n\n'
                        f'Por favor, asegúrese de llegar a tiempo.\n'
                        f'Saludos,\n'
                        f'Equipo de SaludSync'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[paciente.email],
                    fail_silently=False,
                )
                messages.success(self.request, f"Correo enviado exitosamente a {paciente.email}.")
            except Exception as e:
                messages.error(self.request, f"Error al enviar el correo: {str(e)}")

        messages.success(self.request, f"Éxito al crear la Cita Medica del Paciente {form.instance.paciente}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido
        messages.error(self.request, "Error al crear la Cita Medica. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)
    

class Cita_medicaUpdateView(LoginRequiredMixin,UpdateView):
    model = CitaMedica
    template_name = "attention/cita_medica/form.html"
    form_class = Cita_medicaForm
    success_url = reverse_lazy('attention:Cita_medica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Actualizar información de la Cita Medica'  # Cambié el título para que sea más claro
        context['grabar'] = 'Actualizar Cita Medica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # Guarda la instancia del formulario y maneja archivos
        response = super().form_valid(form)
        cita = form.instance  # La cita recién actualizada
        paciente = cita.paciente  # Paciente asociado a la cita
        
        # Verificar si el estado es 'P' (presumiblemente 'Programada')
        if cita.estado == 'P' and paciente.email:  # Solo si el estado es 'P' y el paciente tiene un email registrado
            try:
                send_mail(
                    subject=f'Confirmación de Cita Médica - {paciente.nombres} {paciente.apellidos}',
                    message=(
                        f'Estimado/a {paciente.nombres} {paciente.apellidos},\n\n'
                        f'Su cita médica ha sido actualizada con éxito.\n\n'
                        f'Detalles de la cita:\n'
                        f'- Fecha: {cita.fecha}\n'
                        f'- Hora: {cita.hora_cita}\n'
                        f'- Estado: {cita.estado}\n\n'
                        f'Por favor, asegúrese de llegar a tiempo.\n'
                        f'Saludos,\n'
                        f'Equipo de SaludSync'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[paciente.email],
                    fail_silently=False,
                )
                messages.success(self.request, f"Correo enviado exitosamente a {paciente.email}.")
            except Exception as e:
                messages.error(self.request, f"Error al enviar el correo: {str(e)}")
        else:
            # Si el estado no es 'P' o el paciente no tiene email
            if cita.estado != 'P':
                print(f"No se envió correo. El estado de la cita es: {cita.estado}")
            if not paciente.email:
                print("El paciente no tiene un email registrado.")
        
        # Mensaje de éxito al actualizar la cita médica
        messages.success(self.request, f"Éxito al modificar la Cita Medica del Paciente {paciente}.")
        return response

    def form_invalid(self, form):
        # En caso de que el formulario sea inválido
        messages.error(self.request, "Error al modificar la Cita Medica. Por favor, revisa los datos ingresados.")
        return super().form_invalid(form)


class Cita_medicaDeleteView(LoginRequiredMixin,DeleteView):
    model = CitaMedica
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('attention:Cita_medica_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar la Cita Medica'
        context['description'] = f"¿Desea Eliminar la Cita Medica?: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    

class Cita_medicaDetailView(LoginRequiredMixin,DetailView):
    model = CitaMedica

    def get(self, request, *args, **kwargs):
        try:
            cita = self.get_object()

            paciente_nombre = f"{cita.paciente.nombres} {cita.paciente.apellidos}" if cita.paciente else 'Sin Paciente'
            
            data = {
                'id': cita.id,
                'paciente': paciente_nombre,
                'fecha': cita.fecha,
                'hora_cita': cita.hora_cita,
                'estado': cita.estado,
            }
            return JsonResponse(data)
        except cita.DoesNotExist:
            return JsonResponse({'error': 'Horario de atencion no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return CitaMedica.objects.get(pk=pk)
