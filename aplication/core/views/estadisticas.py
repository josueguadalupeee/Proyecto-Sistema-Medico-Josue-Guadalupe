from django.shortcuts import render
from aplication.core.models import Paciente,Empleado,Cargo
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required
def estadisticas_view(request):
    # Contar los pacientes por género
    masculino_count = Paciente.objects.filter(sexo='M').count()  # Suponiendo que 'M' es masculino
    femenino_count = Paciente.objects.filter(sexo='F').count()  # Suponiendo que 'F' es femenino
    total_count = Paciente.objects.count()

    # Calcular los porcentajes
    if total_count > 0:
        masculino_percentage = (masculino_count / total_count) * 100
        femenino_percentage = (femenino_count / total_count) * 100
    else:
        masculino_percentage = femenino_percentage = 0

    context = {
        'masculino_count': masculino_count,
        'femenino_count': femenino_count,
        'masculino_percentage': masculino_percentage,
        'femenino_percentage': femenino_percentage,
        'total_count': total_count,
    }

    return render(request, 'core/estadisticas/estadisticas.html', context)


# views.py


@login_required
def estadisticas_empleados_view(request):
    # Contar los empleados por cargo
    empleados_por_cargo = Empleado.objects.values('cargo__nombre') \
        .annotate(cantidad=Count('cargo')).order_by('-cantidad')

    context = {
        'empleados_por_cargo': empleados_por_cargo,
    }

    return render(request, 'core/estadisticas/estadisticas_empleados.html', context)
