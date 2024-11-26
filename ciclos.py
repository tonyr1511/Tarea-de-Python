from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Solicitar al usuario ingresar un número
numero = int(input(Fore.GREEN + "Ingrese un número para mostrar su tabla de multiplicar: "))

# Usando ciclo for para mostrar la tabla de multiplicar
print(Fore.CYAN + f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # Ciclo que va del 1 al 10
    print(Fore.YELLOW + f"{numero} x {i} = {numero * i}")

# Usando ciclo while para contar de 1 a 10
print(Fore.MAGENTA + "\nContando del 1 al 10 usando un ciclo while:")
contador = 1
while contador <= 10:
    print(Fore.RED + str(contador))
    contador += 1  # Incrementar el contador
