from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('contactar/<int:producto_id>/', views.contactar_whatsapp, name='contactar_whatsapp'),
    path('registro-productor/', views.registrar_productor, name='registrar_productor'),
    path('publicar-producto/', views.publicar_producto, name='publicar_producto'),
    path('productor/<int:productor_id>/', views.perfil_productor, name='perfil_productor'),
    path('login-productor/', views.login_productor, name='login_productor'),
]