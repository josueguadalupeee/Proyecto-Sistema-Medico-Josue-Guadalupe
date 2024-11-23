from django.views.generic import TemplateView

from aplication.core.models import Paciente
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"title": "SaludSync","title1": "Sistema Medico", "title2": "Sistema Medico"}
        context["can_paci"] = Paciente.cantidad_pacientes()
        print(context["can_paci"])
        return context