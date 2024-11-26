from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Solicitar al usuario ingresar dos números
num1 = float(input(Fore.GREEN + "Ingrese el primer número: "))
num2 = float(input(Fore.GREEN + "Ingrese el segundo número: "))

# Condicionales lógicos
if num1 > 0 and num2 > 0:
    print(Fore.CYAN + "Ambos números son positivos.")
elif num1 < 0 and num2 < 0:
    print(Fore.YELLOW + "Ambos números son negativos.")
elif num1 == 0 or num2 == 0:
    print(Fore.RED + "Al menos uno de los números es cero.")
elif not (num1 > num2):
    print(Fore.MAGENTA + "El primer número no es mayor que el segundo.")
else:
    print(Fore.BLUE + "Condición no especificada.")
