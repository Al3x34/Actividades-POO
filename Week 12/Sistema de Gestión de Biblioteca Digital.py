# ----------------- CLASES -----------------

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.libros = {}      # diccionario: ISBN -> Libro
        self.usuarios = {}    # diccionario: ID -> Usuario
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("✅ Libro agregado.")
        else:
            print("⚠️ El libro ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("✅ Libro eliminado.")
        else:
            print("⚠️ No se encontró el libro.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("✅ Usuario registrado.")
        else:
            print("⚠️ El ID ya existe.")

    def baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("✅ Usuario dado de baja.")
        else:
            print("⚠️ Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"📚 Libro prestado a {usuario.nombre}.")
        else:
            print("⚠️ Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print("✅ Libro devuelto.")
                    return
        print("⚠️ No se pudo devolver el libro.")

    def buscar_libro(self, campo, valor):
        resultados = []
        for libro in self.libros.values():
            if campo == "titulo" and libro.info[0] == valor:
                resultados.append(libro)
            elif campo == "autor" and libro.info[1] == valor:
                resultados.append(libro)
            elif campo == "categoria" and libro.categoria == valor:
                resultados.append(libro)
        return resultados

    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"📚 Libros prestados a {usuario.nombre}:")
                for l in usuario.libros_prestados:
                    print("-", l)
            else:
                print("⚠️ No tiene libros prestados.")
        else:
            print("⚠️ Usuario no encontrado.")


# ----------------- MENÚ -----------------

def menu():
    biblio = Biblioteca()

    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Registrar usuario")
        print("2. Agregar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Listar libros prestados")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblio.registrar_usuario(Usuario(nombre, id_usuario))

        elif opcion == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblio.agregar_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "3":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblio.prestar_libro(id_usuario, isbn)

        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblio.devolver_libro(id_usuario, isbn)

        elif opcion == "5":
            campo = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor: ")
            resultados = biblio.buscar_libro(campo, valor)
            if resultados:
                print("🔍 Resultados:")
                for l in resultados:
                    print("-", l)
            else:
                print("⚠️ No se encontraron libros.")

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            biblio.listar_prestados(id_usuario)

        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida.")


# Ejecutar menú
menu()
