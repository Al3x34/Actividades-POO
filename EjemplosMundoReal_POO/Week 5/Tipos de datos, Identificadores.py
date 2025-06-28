# conversor_temperatura.py
# Este programa convierte una temperatura en grados Celsius a Fahrenheit y Kelvin.
# El usuario ingresa la temperatura en Celsius, y el programa muestra los resultados.

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32  # fórmula para Fahrenheit
    kelvin = celsius + 273.15          # fórmula para Kelvin
    return fahrenheit, kelvin

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Solicitar datos al usuario
entrada_usuario = input("Ingresa la temperatura en grados Celsius: ")

# Validar que sea un número
if es_numero(entrada_usuario):
    temperatura_celsius = float(entrada_usuario)
    temp_fahrenheit, temp_kelvin = convertir_temperatura(temperatura_celsius)

    # Mostrar resultados
    print("Resultado de la conversión:")
    print("Temperatura en Fahrenheit:", temp_fahrenheit)
    print("Temperatura en Kelvin:", temp_kelvin)

    conversion_exitosa = True
else:
    print("Entrada inválida. Debes ingresar un número.")
    conversion_exitosa = False

# Mostrar estado final
print("¿La conversión fue exitosa?", conversion_exitosa)
