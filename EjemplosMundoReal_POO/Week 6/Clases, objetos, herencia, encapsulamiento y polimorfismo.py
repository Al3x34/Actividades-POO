# animal.py

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo encapsulado
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        return "Sonido genérico de animal"

    def descripcion(self):
        return f"{self.get_nombre()} tiene {self.edad} años."


# Clase derivada 1
class Leon(Animal):
    def __init__(self, nombre, edad, melena):
        super().__init__(nombre, edad)
        self.melena = melena

    def hacer_sonido(self):
        return "¡Rugido!"

    def descripcion(self):
        return f"El león {self.get_nombre()} tiene {self.edad} años y melena {self.melena}."


# Clase derivada 2
class Elefante(Animal):
    def __init__(self, nombre, edad, tamaño_colmillos):
        super().__init__(nombre, edad)
        self.tamaño_colmillos = tamaño_colmillos

    def hacer_sonido(self):
        return "¡Brrrroooom!"

    def descripcion(self):
        return f"El elefante {self.get_nombre()} tiene {self.edad} años y colmillos de {self.tamaño_colmillos} cm."


# Programa principal
if __name__ == "__main__":
    # Instancias
    leon1 = Leon("Simba", 5, "larga")
    elefante1 = Elefante("Dumbo", 10, 50)

    # Mostrar información y sonidos
    animales = [leon1, elefante1]

    for animal in animales:
        print(animal.descripcion())
        print("Sonido:", animal.hacer_sonido())
        print("-" * 30)
