# ejemplo_polimorfismo.py

class Ave:
    def hacer_sonido(self):
        print("Sonido de ave")

class Loro(Ave):
    def hacer_sonido(self):
        print("Hola, soy un loro")

class Aguila(Ave):
    def hacer_sonido(self):
        print("Screeeeech!")

# Uso
aves = [Loro(), Aguila()]

for ave in aves:
    ave.hacer_sonido()
