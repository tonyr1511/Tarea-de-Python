from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Solicitar al usuario dos números
num1 = float(input(Fore.GREEN + "Ingrese el primer número: "))
num2 = float(input(Fore.GREEN + "Ingrese el segundo número: "))

# Comparaciones
if num1 == num2:
    print(Fore.CYAN + "Los números son iguales.")
elif num1 != num2:
    print(Fore.YELLOW + "Los números son diferentes.")
elif num1 > num2:
    print(Fore.RED + "El primer número es mayor que el segundo.")
elif num1 < num2:
    print(Fore.RED + "El primer número es menor que el segundo.")
elif num1 >= num2:
    print(Fore.MAGENTA + "El primer número es mayor o igual que el segundo.")
elif num1 <= num2:
    print(Fore.MAGENTA + "El primer número es menor o igual que el segundo.")
