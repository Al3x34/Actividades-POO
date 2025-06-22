# ---------------------------------------------------------------
# Finalidad del programa:
# Este programa simula una tienda sencilla del mundo real usando
# Programación Orientada a Objetos (POO). Se crean clases para
# representar productos y una tienda. Sirve para aprender cómo
# funcionan los objetos, atributos y métodos en Python.
# ---------------------------------------------------------------

# Creamos la clase Producto
class Producto:
    # Método constructor: se ejecuta al crear un objeto Producto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre     # Nombre del producto
        self.precio = precio     # Precio del producto
        self.stock = stock       # Cantidad disponible (inventario)

    # Método para mostrar información del producto
    def mostrar(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}")

# Creamos la clase Tienda
class Tienda:
    # Método constructor: recibe el nombre de la tienda
    def __init__(self, nombre):
        self.nombre = nombre      # Nombre de la tienda
        self.productos = []       # Lista vacía para guardar productos

    # Método para agregar productos a la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)  # Añade el producto a la lista

    # Método para mostrar todos los productos disponibles
    def mostrar_productos(self):
        print(f"Productos disponibles en la tienda {self.nombre}:")
        for producto in self.productos:
            producto.mostrar()    # Llama al método mostrar() de cada producto
        print()

    # Método para vender un producto
    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad   # Resta el stock
                    total = producto.precio * cantidad
                    print(f"\nCompra exitosa. Total a pagar: ${total}\n")
                else:
                    print("\nNo hay suficiente stock disponible.\n")
                return
        print("\nProducto no encontrado.\n")

# -----------------------------
# Parte principal del programa
# -----------------------------

# Creamos un objeto Tienda
mi_tienda = Tienda("Mi Tiendita")

# Creamos productos usando la clase Producto
producto1 = Producto("Manzana", 0.5, 20)
producto2 = Producto("Pan", 0.3, 15)

# Agregamos productos a la tienda
mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

# Mostramos los productos antes de la compra
mi_tienda.mostrar_productos()

# Simulamos una compra (3 manzanas)
mi_tienda.vender_producto("Manzana", 3)

# Mostramos los productos después de la compra
mi_tienda.mostrar_productos()
