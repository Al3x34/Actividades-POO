# Creamos una clase para representar un Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Estos son los atributos de cada producto
        self.nombre = nombre      # Nombre del producto
        self.precio = precio      # Precio del producto
        self.stock = stock        # Cantidad disponible del producto

    # Método para mostrar información del producto
    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}")

    # Método para reducir el stock cuando se vende
    def reducir_stock(self, cantidad):
        # Si hay suficiente en stock, se descuenta
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            # Si no hay suficiente, no se puede vender
            return False

# Creamos otra clase para representar la Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre      # Nombre de la tienda
        self.productos = []       # Lista vacía donde se guardarán los productos

    # Método para agregar productos a la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar todos los productos disponibles
    def mostrar_productos(self):
        print(f"\nProductos disponibles en la tienda {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()  # Llamamos al método mostrar_info de cada producto

    # Método para vender un producto
    def vender_producto(self, nombre_producto, cantidad):
        # Buscamos el producto en la lista de productos
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():  # Comparamos sin importar mayúsculas
                if producto.reducir_stock(cantidad):
                    total = producto.precio * cantidad
                    print(f"\nCompra exitosa. Total a pagar: ${total}")
                else:
                    print("\nNo hay suficiente stock para esta cantidad.")
                return  # Salimos del método después de encontrar el producto
        print("\nProducto no encontrado en la tienda.")

# Aquí empieza el código principal que se ejecuta
if __name__ == "__main__":
    # Creamos una tienda llamada "Mi Tiendita"
    mi_tienda = Tienda("Mi Tiendita")

    # Creamos algunos productos con nombre, precio y stock
    producto1 = Producto("Manzana", 0.50, 20)
    producto2 = Producto("Pan", 0.30, 15)

    # Agregamos los productos a la tienda
    mi_tienda.agregar_producto(producto1)
    mi_tienda.agregar_producto(producto2)

    # Mostramos los productos disponibles antes de la compra
    mi_tienda.mostrar_productos()

    # Simulamos una compra: queremos comprar 3 manzanas
    mi_tienda.vender_producto("Manzana", 3)

    # Mostramos los productos después de la compra para ver el nuevo stock
    mi_tienda.mostrar_productos()
