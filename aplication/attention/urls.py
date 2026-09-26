from django.urls import path

from aplication.attention.views.horario_atencion import Horario_AtencionListView, Horario_AtencionCreateView, Horario_AtencionUpdateView, Horario_AtencionDeleteView, Horario_AtencionDetailView
from aplication.attention.views.cita_medica import Cita_medicaListView, Cita_medicaCreateView, Cita_medicaUpdateView, Cita_medicaDeleteView, Cita_medicaDetailView
from aplication.attention.views.examen_solicitado import Examen_solicitadoListView, Examen_solicitadoCreateView, Examen_solicitadoUpdateView, Examen_solicitadoDeleteView, Examen_solicitadoDetailView
from aplication.attention.views.servicios_adicionales import Servicios_adicionalesListView, Servicios_adicionalesCreateView, Servicios_adicionalesUpdateView, Servicios_adicionalesDeleteView, Servicios_adicionalesDetailView
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView


app_name='attention'

urlpatterns= [
    path('Horario_atencion_list/',Horario_AtencionListView.as_view() ,name="Horario_atencion_list"),
    path('Horario_atencion_create/', Horario_AtencionCreateView.as_view(),name="Horario_atencion_create"),
    path('Horario_atencion_update/<int:pk>/', Horario_AtencionUpdateView.as_view(),name='Horario_atencion_update'),
    path('Horario_atencion_delete/<int:pk>/', Horario_AtencionDeleteView.as_view(),name='Horario_atencion_delete'),
    path('Horario_atencion_detail/<int:pk>/', Horario_AtencionDetailView.as_view(), name='Horario_atencion_detail'),
    path('Cita_medica_list/',Cita_medicaListView.as_view() ,name="Cita_medica_list"),
    path('Cita_medica_create/', Cita_medicaCreateView.as_view(),name="Cita_medica_create"),
    path('Cita_medica_update/<int:pk>/', Cita_medicaUpdateView.as_view(),name='Cita_medica_update'),
    path('Cita_medica_delete/<int:pk>/', Cita_medicaDeleteView.as_view(),name='Cita_medica_delete'),
    path('Cita_medica_detail/<int:pk>/', Cita_medicaDetailView.as_view(), name='Cita_medica_detail'),
    path('Examen_solicitado_list/',Examen_solicitadoListView.as_view() ,name="Examen_solicitado_list"),
    path('Examen_solicitado_create/', Examen_solicitadoCreateView.as_view(),name="Examen_solicitado_create"),
    path('Examen_solicitado_update/<int:pk>/', Examen_solicitadoUpdateView.as_view(),name='Examen_solicitado_update'),
    path('Examen_solicitado_delete/<int:pk>/', Examen_solicitadoDeleteView.as_view(),name='Examen_solicitado_delete'),
    path('Examen_solicitado_detail/<int:pk>/', Examen_solicitadoDetailView.as_view(), name='Examen_solicitado_detail'),
    path('Servicios_adicionales_list/',Servicios_adicionalesListView.as_view() ,name="Servicios_adicionales_list"),
    path('Servicios_adicionales_create/', Servicios_adicionalesCreateView.as_view(),name="Servicios_adicionales_create"),
    path('Servicios_adicionales_update/<int:pk>/', Servicios_adicionalesUpdateView.as_view(),name='Servicios_adicionales_update'),
    path('Servicios_adicionales_delete/<int:pk>/', Servicios_adicionalesDeleteView.as_view(),name='Servicios_adicionales_delete'),
    path('Servicios_adicionales_detail/<int:pk>/', Servicios_adicionalesDetailView.as_view(), name='Servicios_adicionales_detail'),
    path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
    path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
    path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
    path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
        
]