from django.contrib import admin
from .models import Productor, Categoria, Producto, Contacto

@admin.register(Productor)
class ProductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'vereda', 'correo')
    search_fields = ('nombre', 'vereda')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'productor', 'fecha_publicacion')
    list_filter = ('categoria', 'productor')
    search_fields = ('nombre', 'descripcion')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'medio_contacto', 'fecha_contacto')
    list_filter = ('medio_contacto', 'fecha_contacto')