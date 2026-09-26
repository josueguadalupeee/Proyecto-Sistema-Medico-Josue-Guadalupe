from django.urls import path
from aplication.core.views.estadisticas import estadisticas_view,estadisticas_empleados_view
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.tipo_sangre import Tipo_sangreCreateView, Tipo_sangrelistview, Tipo_sangreUpdateView, Tipo_sangreDeleteView
from aplication.core.views.especialidad import Especialidad_CreateView, Especialidad_UpdateView, Especialidad_ListView, Especialidad_DeleteView
from aplication.core.views.doctor import Doctor_ListView, Doctor_UpdateView, Doctor_CreateView, Doctor_DeleteView, DoctorDetailView
from aplication.core.views.cargo import Cargo_ListView, Cargo_CreateView, Cargo_UpdateView, Cargo_DeleteView, Cargo_DetailView
from aplication.core.views.empleado import Empleado_ListView, Empleado_CreateView, Empleado_UpdateView, Empleado_DeleteView, Empleado_DetailView
from aplication.core.views.tipo_medicamento import Tipo_Medicamento_ListView, Tipo_Medicamento_CreateView, Tipo_Medicamento_UpdateView, Tipo_Medicamento_DeleteView, Tipo_Medicamento_DetailView
from aplication.core.views.marca_medicamento import Marca_Medicamento_ListView, Marca_Medicamento_CreateView, Marca_Medicamento_UpdateView, Marca_Medicamento_DeleteView, Marca_Medicamento_DetailView
from aplication.core.views.medicamento import Medicamento_ListView, Medicamento_CreateView, Medicamento_UpdateView, Medicamento_DeleteView, Medicamento_DetailView
from aplication.core.views.diagnostico import Diagnostico_ListView, Diagnostico_CreateView,  Diagnostico_UpdateView, Diagnostico_DeleteView, Diagnostico_DetailView
from aplication.core.views.categoria_examen import Categoria_examen_ListView, Categoria_examen_CreateView,  Categoria_examen_UpdateView, Categoria_examen_DeleteView, Categoria_examen_DetailView
from aplication.core.views.tipo_categoria import Tipo_Categoria_ListView, Tipo_Categoria_CreateView,  Tipo_Categoria_UpdateView, Tipo_Categoria_DeleteView, Tipo_Categoria_DetailView
from aplication.core.views.auditoria import  Auditoria_ListView, Auditoria_DetailView
app_name='core'

urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores VBF
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  path('tipo_sangre_list/',Tipo_sangrelistview.as_view() ,name="tipo_sangre_list"),
  path('tipo_sangre_create/', Tipo_sangreCreateView.as_view(),name="tipo_sangre_create"),
  path('tipo_sangre_update/<int:pk>/', Tipo_sangreUpdateView.as_view(),name='tipo_sangre_update'),
  path('tipo_sangre_delete/<int:pk>/', Tipo_sangreDeleteView.as_view(),name='tipo_sangre_delete'),
  path('Especialidad_list/',Especialidad_ListView.as_view() ,name="Especialidad_list"),
  path('Especialidad_create/', Especialidad_CreateView.as_view(),name="Especialidad_create"),
  path('Especialidad_update/<int:pk>/', Especialidad_UpdateView.as_view(),name='Especialidad_update'),
  path('Especialidad_delete/<int:pk>/', Especialidad_DeleteView.as_view(),name='Especialidad_delete'),
  path('doctor_list/',Doctor_ListView.as_view() ,name="doctor_list"),
  path('Doctor_create/', Doctor_CreateView.as_view(),name="Doctor_create"),
  path('Doctor_update/<int:pk>/', Doctor_UpdateView.as_view(),name='Doctor_update'),
  path('Doctor_delete/<int:pk>/', Doctor_DeleteView.as_view(),name='Doctor_delete'),
  path('Doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='Doctor_detail'),
  path('Cargo_list/',Cargo_ListView.as_view() ,name="Cargo_list"),
  path('Cargo_create/', Cargo_CreateView.as_view(),name="Cargo_create"),
  path('Cargo_update/<int:pk>/', Cargo_UpdateView.as_view(),name='Cargo_update'),
  path('Cargo_delete/<int:pk>/', Cargo_DeleteView.as_view(),name='Cargo_delete'),
  path('Cargo_detail/<int:pk>/', Cargo_DetailView.as_view(), name='Cargo_detail'),
  path('Empleado_list/',Empleado_ListView.as_view() ,name="Empleado_list"),
  path('Empleado_create/', Empleado_CreateView.as_view(),name="Empleado_create"),
  path('Empleado_update/<int:pk>/', Empleado_UpdateView.as_view(),name='Empleado_update'),
  path('Empleado_delete/<int:pk>/', Empleado_DeleteView.as_view(),name='Empleado_delete'),
  path('Empleado_detail/<int:pk>/', Empleado_DetailView.as_view(), name='Empleado_detail'),
  path('Tipo_medicamento_list/',Tipo_Medicamento_ListView.as_view() ,name="Tipo_medicamento_list"),
  path('Tipo_medicamento_create/', Tipo_Medicamento_CreateView.as_view(),name="Tipo_medicamento_create"),
  path('Tipo_medicamento_update/<int:pk>/', Tipo_Medicamento_UpdateView.as_view(),name='Tipo_medicamento_update'),
  path('Tipo_medicamento_delete/<int:pk>/', Tipo_Medicamento_DeleteView.as_view(),name='Tipo_medicamento_delete'),
  path('Tipo_medicamento_detail/<int:pk>/', Tipo_Medicamento_DetailView.as_view(), name='Tipo_medicamento_detail'),
  path('Marca_medicamento_list/',Marca_Medicamento_ListView.as_view() ,name="Marca_medicamento_list"),
  path('Marca_medicamento_create/', Marca_Medicamento_CreateView.as_view(),name="Marca_medicamento_create"),
  path('Marca_medicamento_update/<int:pk>/', Marca_Medicamento_UpdateView.as_view(),name='Marca_medicamento_update'),
  path('Marca_medicamento_delete/<int:pk>/', Marca_Medicamento_DeleteView.as_view(),name='Marca_medicamento_delete'),
  path('Marca_medicamento_detail/<int:pk>/', Marca_Medicamento_DetailView.as_view(), name='Marca_medicamento_detail'),
  path('Medicamento_list/',Medicamento_ListView.as_view() ,name="Medicamento_list"),
  path('Medicamento_create/', Medicamento_CreateView.as_view(),name="Medicamento_create"),
  path('Medicamento_update/<int:pk>/', Medicamento_UpdateView.as_view(),name='Medicamento_update'),
  path('Medicamento_delete/<int:pk>/', Medicamento_DeleteView.as_view(),name='Medicamento_delete'),
  path('Medicamento_detail/<int:pk>/', Medicamento_DetailView.as_view(), name='Medicamento_detail'),
  path('Diagnostico_list/',Diagnostico_ListView.as_view() ,name="Diagnostico_list"),
  path('Diagnostico_create/', Diagnostico_CreateView.as_view(),name="Diagnostico_create"),
  path('Diagnostico_update/<int:pk>/', Diagnostico_UpdateView.as_view(),name='Diagnostico_update'),
  path('Diagnostico_delete/<int:pk>/', Diagnostico_DeleteView.as_view(),name='Diagnostico_delete'),
  path('Diagnostico_detail/<int:pk>/', Diagnostico_DetailView.as_view(), name='Diagnostico_detail'),
  path('Categoria_examen_list/',Categoria_examen_ListView.as_view() ,name="Categoria_examen_list"),
  path('Categoria_examen_create/', Categoria_examen_CreateView.as_view(),name="Categoria_examen_create"),
  path('Categoria_examen_update/<int:pk>/', Categoria_examen_UpdateView.as_view(),name='Categoria_examen_update'),
  path('Categoria_examen_delete/<int:pk>/', Categoria_examen_DeleteView.as_view(),name='Categoria_examen_delete'),
  path('Categoria_examen_detail/<int:pk>/', Categoria_examen_DetailView.as_view(), name='Categoria_examen_detail'),
  path('Tipo_categoria_list/',Tipo_Categoria_ListView.as_view() ,name="Tipo_categoria_list"),
  path('Tipo_categoria_create/', Tipo_Categoria_CreateView.as_view(),name="Tipo_categoria_create"),
  path('Tipo_categoria_update/<int:pk>/', Tipo_Categoria_UpdateView.as_view(),name='Tipo_categoria_update'),
  path('Tipo_categoria_delete/<int:pk>/', Tipo_Categoria_DeleteView.as_view(),name='Tipo_categoria_delete'),
  path('Tipo_categoria_detail/<int:pk>/', Tipo_Categoria_DetailView.as_view(), name='Tipo_categoria_detail'),
  path('Auditoria_list/', Auditoria_ListView.as_view(), name='Auditoria_list'),
  path('Auditoria_detail/<int:pk>/', Auditoria_DetailView.as_view(), name='Auditoria_detail'),
  path('estadisticas/', estadisticas_view, name='estadisticas'),
  path('estadisticas_empleados/', estadisticas_empleados_view, name='estadisticas_empleados'),
  # path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
]