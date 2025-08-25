# Sistema de Gestión de Inventarios Mejorado
# Autor: Steven Castro
# Descripción: Este programa maneja un inventario de productos utilizando archivos de texto
# y aplica manejo de excepciones para evitar fallos en la lectura/escritura.

import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa"""
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        self.productos.append(Producto(id, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará uno nuevo al guardar productos.")
        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"⚠️ Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos actuales en el archivo"""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"⚠️ Error al guardar en el archivo: {e}")

    def añadir_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido y guardado en el archivo.")

    def actualizar_producto(self, id, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.id == id:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print("✅ Producto actualizado y guardado en el archivo.")
                return
        print("⚠️ Producto no encontrado.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("✅ Producto eliminado y archivo actualizado.")
                return
        print("⚠️ Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📂 El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for p in self.productos:
                print(f"ID: {p.id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: {p.precio}")


# --- Interfaz de usuario en consola ---
def menu():
    inventario = Inventario()

    while True:
        print("\n📌 Menú de Gestión de Inventario")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(Producto(id, nombre, cantidad, precio))
            except ValueError:
                print("⚠️ Error: la cantidad debe ser un número entero y el precio un número decimal.")

        elif opcion == "2":
            id = input("ID del producto a actualizar: ")
            try:
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("⚠️ Error: datos inválidos.")

        elif opcion == "3":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
