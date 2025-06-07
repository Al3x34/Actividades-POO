# ejemplo_encapsulacion.py

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.__edad}")

    def cambiar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

# Uso
p1 = Persona("Ana", 20)
p1.mostrar_info()

# Intentamos cambiar la edad con un valor válido
p1.cambiar_edad(25)
p1.mostrar_info()

# Intentamos acceder directamente (no recomendado)
# print(p1.__edad)  # Esto daría error
