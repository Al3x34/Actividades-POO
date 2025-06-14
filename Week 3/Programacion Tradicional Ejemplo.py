# Este programa pide las temperaturas de 7 días y calcula el promedio usando funciones

# Función para ingresar temperaturas
def ingresar_temperaturas():
    temperaturas = []  # Lista vacía para guardar las temperaturas
    for dia in range(1, 8):  # Repetimos 7 veces, un día por cada número del 1 al 7
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))  # Pedimos temperatura
        temperaturas.append(temp)  # Agregamos la temperatura a la lista
    return temperaturas  # Devolvemos la lista completa

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)  # Sumamos todas las temperaturas
    promedio = suma / len(temperaturas)  # Dividimos por la cantidad (7)
    return promedio  # Devolvemos el promedio

# Función principal (donde se usa todo lo anterior)
def main():
    print("PROMEDIO DE TEMPERATURAS - Modo Tradicional")
    temperaturas = ingresar_temperaturas()  # Llamamos la función para obtener las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calculamos el promedio
    print(f"El promedio de la semana es: {promedio:.2f}°C")  # Mostramos el resultado

# Llamamos a la función principal para iniciar el programa
main()

