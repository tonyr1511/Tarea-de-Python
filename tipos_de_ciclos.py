from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Función de simulación de un ciclo "do-while" en Python
def do_while_example():
    # Ciclo que se ejecuta al menos una vez, similar a "do-while"
    counter = 1
    while True:  # La condición se revisa después de ejecutar
        print(Fore.GREEN + f"Ciclo do-while: Iteración {counter}")
        counter += 1
        if counter > 5:  # Condición de salida
            break

# 1. Usando ciclo for
print(Fore.CYAN + "Ciclo for: Iterando sobre una lista de números del 1 al 5:")
for i in range(1, 6):  # Ciclo for básico
    print(Fore.YELLOW + f"Valor: {i}")

# 2. Simulando un ciclo foreach (en Python, usamos un ciclo for para iterar sobre una colección)
print(Fore.MAGENTA + "\nCiclo foreach: Iterando sobre una lista de nombres:")
nombres = ["Ana", "Juan", "Pedro", "Maria"]
for nombre in nombres:  # Iteración sobre los elementos de la lista
    print(Fore.RED + f"Nombre: {nombre}")

# 3. Usando ciclo while
print(Fore.CYAN + "\nCiclo while: Contando hasta el 5:")
contador = 1
while contador <= 5:  # Ciclo while, se ejecuta mientras la condición sea True
    print(Fore.GREEN + f"Contador: {contador}")
    contador += 1

# 4. Simulando un ciclo do-while (con una condición al final)
print(Fore.BLUE + "\nCiclo do-while (simulado):")
do_while_example()
