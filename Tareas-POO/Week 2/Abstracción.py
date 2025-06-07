# ejemplo_abstraccion.py

from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# Clase concreta que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Usamos las clases
perro = Perro()
gato = Gato()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
