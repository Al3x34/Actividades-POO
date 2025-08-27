import json

class Producto:
    def __init__(self, id_, nombre, cantidad, precio):
        self.id = id_
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre,
                "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(d):
        return Producto(d["id"], d["nombre"], d["cantidad"], d["precio"])


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, p: Producto):
        if p.id in self.productos:
            return False
        self.productos[p.id] = p
        return True

    def eliminar(self, id_):
        return self.productos.pop(id_, None)

    def actualizar(self, id_, nombre=None, cantidad=None, precio=None):
        if id_ not in self.productos:
            return False
        p = self.productos[id_]
        if nombre: p.nombre = nombre
        if cantidad is not None: p.cantidad = cantidad
        if precio is not None: p.precio = precio
        return True

    def buscar(self, nombre):
        return [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_todos(self):
        return list(self.productos.values())

    def guardar(self, archivo="inventario.json"):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump({pid: p.to_dict() for pid, p in self.productos.items()}, f, indent=2)

    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.productos = {pid: Producto.from_dict(p) for pid, p in data.items()}
        except FileNotFoundError:
            pass


def menu():
    inv = Inventario()
    inv.cargar()

    while True:
        print("\n1) Añadir  2) Eliminar  3) Actualizar  4) Buscar  5) Mostrar  6) Guardar  0) Salir")
        op = input("Opción: ")

        if op == "1":
            pid = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            if inv.agregar(Producto(pid, nombre, cantidad, precio)):
                print("✅ Agregado")
            else:
                print("❌ ID ya existe")

        elif op == "2":
            pid = input("ID a eliminar: ")
            print("🗑️ Eliminado" if inv.eliminar(pid) else "❌ No encontrado")

        elif op == "3":
            pid = input("ID a actualizar: ")
            nombre = input("Nuevo nombre (Enter = no cambia): ")
            cant = input("Nueva cantidad (Enter = no cambia): ")
            prec = input("Nuevo precio (Enter = no cambia): ")
            ok = inv.actualizar(pid,
                                nombre or None,
                                int(cant) if cant else None,
                                float(prec) if prec else None)
            print("✏️ Actualizado" if ok else "❌ No encontrado")

        elif op == "4":
            nombre = input("Nombre a buscar: ")
            res = inv.buscar(nombre)
            for p in res: print(p.to_dict())
            if not res: print("❌ No encontrado")

        elif op == "5":
            for p in inv.mostrar_todos(): print(p.to_dict())

        elif op == "6":
            inv.guardar()
            print("💾 Inventario guardado")

        elif op == "0":
            inv.guardar()
            print("👋 Adiós")
            break
        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()