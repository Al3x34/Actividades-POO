class Persona:
    # Constructor: se llama automáticamente al crear un objeto de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"[Constructor] Se creó la persona: {self.nombre}, {self.edad} años")

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    # Destructor: se llama automáticamente cuando el objeto se elimina
    def __del__(self):
        print(f"[Destructor] Se eliminó la persona: {self.nombre}")


# Ejecución principal
if __name__ == "__main__":
    persona1 = Persona("Luis", 25)  # Se ejecuta el constructor
    persona1.saludar()

    print("Este es el final del programa. La persona será eliminada.")
    # Al final del programa, Python eliminará automáticamente el objeto y llamará al destructor
