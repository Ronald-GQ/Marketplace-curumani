from django.db import models

class Productor(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Usuario / Productor")
    contrasena = models.CharField(max_length=100, default="123456", verbose_name="Contraseña") # Clave para acceder
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(blank=True, null=True)
    vereda = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    fecha_contacto = models.DateTimeField(auto_now_add=True)
    medio_contacto = models.CharField(max_length=50, default="WhatsApp")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contacto para {self.producto.nombre} - {self.fecha_contacto.strftime('%Y-%m-%d')}"
