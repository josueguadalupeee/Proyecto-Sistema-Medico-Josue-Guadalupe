# views.py
from aplication.core.models import AuditUser
from django.utils import timezone
from django.forms import ValidationError
from django.urls import reverse_lazy
from aplication.core.forms.cargo import Cargo_Form
from aplication.core.models import Cargo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.db.models import Q

class Auditoria_ListView(LoginRequiredMixin,ListView):
    model = AuditUser
    template_name = 'core/auditoria/list.html'  # Asegúrate de que este template existe
    context_object_name = 'auditorias'
    paginate_by = 10  # Puedes ajustar la cantidad de registros por página

    def get_queryset(self):
        # Si deseas obtener las auditorías solo para el día actual, puedes filtrar por la fecha de hoy.
        # Si no deseas este filtro, puedes omitir esta parte.
        # queryset = AuditUser.objects.filter(fecha=timezone.now().date())
        return AuditUser.objects.all().order_by('-fecha', '-hora')  # Ordenar por fecha y hora descendentes







class Auditoria_DetailView(LoginRequiredMixin,DetailView):
    model = AuditUser

    def get(self, request, *args, **kwargs):
        try:
            audit_user = self.get_object()
            data = {
                'id': audit_user.id,
                'usuario': audit_user.usuario.username,
                'tabla': audit_user.tabla,
                'registroid': audit_user.registroid,
                'accion': audit_user.accion,
                'fecha': audit_user.fecha.isoformat(),
                'hora': audit_user.hora.strftime('%H:%M:%S'),
                'estacion': audit_user.estacion,
            }
            return JsonResponse(data)
        except AuditUser.DoesNotExist:
            return JsonResponse({'error': 'Auditoría no encontrada'}, status=404)

