from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Función que recibe un parámetro y muestra un mensaje
def saludo(nombre):
    print(Fore.GREEN + f"¡Hola, {nombre}! Bienvenido al programa.")

# Función que recibe dos parámetros y suma sus valores
def suma(a, b):
    resultado = a + b
    return resultado

# Función que recibe tres parámetros y calcula el promedio
def promedio(a, b, c):
    return (a + b + c) / 3

# Función principal que pide datos al usuario y usa los parámetros
def programa():
    print(Fore.CYAN + "¡Bienvenido al programa de ejemplo con parámetros!")
    
    # Pedimos el nombre para saludar
    nombre = input(Fore.YELLOW + "Por favor, ingresa tu nombre: ")
    saludo(nombre)
    
    # Pedimos dos números para sumarlos
    num1 = float(input(Fore.YELLOW + "Ingresa el primer número: "))
    num2 = float(input(Fore.YELLOW + "Ingresa el segundo número: "))
    resultado_suma = suma(num1, num2)
    print(Fore.MAGENTA + f"La suma de {num1} y {num2} es: {resultado_suma}")
    
    # Pedimos tres números para calcular el promedio
    num3 = float(input(Fore.YELLOW + "Ingresa el tercer número: "))
    resultado_promedio = promedio(num1, num2, num3)
    print(Fore.MAGENTA + f"El promedio de {num1}, {num2} y {num3} es: {resultado_promedio:.2f}")

# Llamamos a la función principal para ejecutar el programa
programa()
