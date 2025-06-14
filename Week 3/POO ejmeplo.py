# Este programa hace lo mismo, pero usando clases y objetos

# Creamos una clase para representar el clima de la semana
class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Creamos una lista para guardar las temperaturas

    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))  # Pedimos temperatura
            self.temperaturas.append(temp)  # La agregamos a la lista

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0  # Por si no hay datos
        return sum(self.temperaturas) / len(self.temperaturas)  # Devolvemos el promedio

# Clase hija para mostrar herencia (extiende la clase anterior)
class ClimaExtendido(ClimaSemanal):
    def mostrar_temperaturas(self):
        print("Temperaturas ingresadas:", self.temperaturas)  # Muestra la lista completa

# Función principal
def main():
    print("PROMEDIO DE TEMPERATURAS - Modo POO")
    clima = ClimaExtendido()  # Creamos un objeto (instancia) de la clase
    clima.ingresar_temperaturas()  # Llamamos el método para ingresar temperaturas
    clima.mostrar_temperaturas()  # Mostramos las temperaturas ingresadas
    promedio = clima.calcular_promedio()  # Calculamos el promedio usando el método
    print(f"El promedio de la semana es: {promedio:.2f}°C")  # Mostramos el resultado

# Iniciamos el programa
main()
