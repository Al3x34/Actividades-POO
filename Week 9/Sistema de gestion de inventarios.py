# ===============================
# Sistema de Gestión de Inventarios
# Autor: Steven Castro (estudiante)
# ===============================

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor: inicializa los atributos
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para representar el producto como texto
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        # Lista que guardará objetos de tipo Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Validar que el ID no se repita
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑️ Producto eliminado correctamente.")
                return
        print("❌ No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado correctamente.")
                return
        print("❌ No se encontró el producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔎 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Lista de productos en el inventario:")
            for p in self.productos:
                print(p)


# ===============================
# Interfaz de Usuario (Menú)
# ===============================

def menu():
    inventario = Inventario()

    while True:
        print("\n=== Menú de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            nuevo = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Nuevo precio (deje vacío si no desea cambiar): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida, intente de nuevo.")


# Ejecutar el menú solo si es el programa principal
if __name__ == "__main__":
    menu()