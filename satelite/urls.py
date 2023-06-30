from django.urls import path
from . import views

app_name = 'satelite'

urlpatterns = [
    path('', views.satelite_views, name='satelite_views'),
    path('localizacion_por_partes/<str:nombre_antena>/', views.localizacion_por_partes_views, name='localizacion_por_partes_views'),
    # Otras URLs de la aplicación "satelite"...
]