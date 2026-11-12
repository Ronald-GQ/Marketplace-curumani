from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Contacto

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    productos = Producto.objects.all().order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    return render(request, 'plataforma/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None
    })

def contactar_whatsapp(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    # Registramos el contacto en la base de datos (cumple con la entidad Contacto)
    Contacto.objects.create(
        producto=producto,
        medio_contacto="WhatsApp"
    )

    # Limpiamos el número de teléfono
    telefono = producto.productor.telefono.replace(" ", "").replace("+", "")
    if not telefono.startswith("57"):
        telefono = f"57{telefono}"

    mensaje = f"Hola {producto.productor.nombre}, estoy interesado en tu producto '{producto.nombre}' publicado en la plataforma de comercio rural de curumaní."
    url_whatsapp = f"https://wa.me/{telefono}?text={mensaje.replace(' ', '%20')}"
    
    return redirect(url_whatsapp)