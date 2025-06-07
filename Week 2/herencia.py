# ejemplo_herencia.py

# Clase base
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"{self.marca} está encendido.")

# Clase hija
class Auto(Vehiculo):
    def tocar_bocina(self):
        print("Beep beep!")

# Uso
mi_auto = Auto("Toyota")
mi_auto.encender()
mi_auto.tocar_bocina()
