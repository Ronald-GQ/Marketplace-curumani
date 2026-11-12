from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Productor, Producto, Categoria, Contacto
from django.contrib import messages
from .forms import ProductorForm, ProductoForm

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    query = request.GET.get('buscar') # Captura el texto de la barra de búsqueda
    
    productos = Producto.objects.all().order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()

    # Filtro por categoría
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    # Filtro por término de búsqueda (en nombre o descripción)
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    return render(request, 'plataforma/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None,
        'query': query, # Mantiene el texto escrito en el input de búsqueda
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

def registrar_productor(request):
    if request.method == 'POST':
        form = ProductorForm(request.POST)
        if form.is_valid():
            productor = form.save()
            messages.success(request, f'¡Bienvenido {productor.nombre}! Este es tu panel de productor.')
            # Ahora redirige directo a SU perfil usando su ID
            return redirect('perfil_productor', productor_id=productor.id)
    else:
        form = ProductorForm()
    
    return render(request, 'plataforma/registro_productor.html', {'form': form})

def perfil_productor(request, productor_id):
    productor = get_object_or_404(Productor, pk=productor_id)
    # Filtramos solo los productos que pertenecen a este productor
    mis_productos = Producto.objects.filter(productor=productor).order_by('-fecha_publicacion')
    
    return render(request, 'plataforma/perfil_productor.html', {
        'productor': productor,
        'productos': mis_productos
    })

def publicar_producto(request):
    # Capturamos si viene el ID del productor desde su perfil para preseleccionarlo
    productor_id = request.GET.get('productor')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'¡Producto "{producto.nombre}" publicado exitosamente!')
            # Al publicar, vuelve directo al perfil de ese productor para verlo en su lista
            return redirect('perfil_productor', productor_id=producto.productor.id)
    else:
        # Si viene desde un perfil, preseleccionamos su nombre en el formulario
        initial_data = {'productor': productor_id} if productor_id else {}
        form = ProductoForm(initial=initial_data)
        
    return render(request, 'plataforma/publicar_producto.html', {'form': form})


def login_productor(request):
    if request.method == 'POST':
        usuario = request.POST.get('nombre')
        passw = request.POST.get('contrasena')
        
        try:
            productor = Productor.objects.get(nombre=usuario, contrasena=passw)
            messages.success(request, f'¡Bienvenido de nuevo, {productor.nombre}!')
            return redirect('perfil_productor', productor_id=productor.id)
        except Productor.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos. Inténtalo de nuevo.')
            
    return render(request, 'plataforma/login_productor.html')