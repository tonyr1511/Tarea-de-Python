from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Solicitar al usuario dos números
num1 = float(input(Fore.GREEN + "Ingrese el primer número: "))
num2 = float(input(Fore.GREEN + "Ingrese el segundo número: "))

# Operaciones Aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
division_entera = num1 // num2
exponente = num1 ** num2

# Imprimir resultados
print(Fore.CYAN + f"La suma de {num1} + {num2} es: {suma}")
print(Fore.YELLOW + f"La resta de {num1} - {num2} es: {resta}")
print(Fore.RED + f"La multiplicación de {num1} * {num2} es: {multiplicacion}")
print(Fore.MAGENTA + f"La división de {num1} / {num2} es: {division}")
print(Fore.BLUE + f"El módulo de {num1} % {num2} es: {modulo}")
print(Fore.GREEN + f"La división entera de {num1} // {num2} es: {division_entera}")
print(Fore.WHITE + f"{num1} elevado a {num2} (exponente) es: {exponente}")
