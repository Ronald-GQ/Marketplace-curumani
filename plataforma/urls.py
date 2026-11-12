from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('contactar/<int:producto_id>/', views.contactar_whatsapp, name='contactar_whatsapp'),
]