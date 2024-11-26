from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# 1. Lista
print(Fore.CYAN + "Ejemplo de Lista:")
mi_lista = ["manzana", "banana", "cereza", "durazno", "kiwi"]
print(Fore.YELLOW + "Lista original:", mi_lista)

# Agregar un elemento a la lista
mi_lista.append("uva")
print(Fore.GREEN + "Lista después de agregar un elemento:", mi_lista)

# Eliminar un elemento de la lista
mi_lista.remove("banana")
print(Fore.RED + "Lista después de eliminar un elemento:", mi_lista)

# 2. Tupla
print(Fore.CYAN + "\nEjemplo de Tupla:")
mi_tupla = ("rojo", "verde", "azul")
print(Fore.YELLOW + "Tupla original:", mi_tupla)

# Intentar modificar una tupla (esto genera un error porque las tuplas son inmutables)
try:
    mi_tupla[0] = "amarillo"
except TypeError as e:
    print(Fore.RED + f"Error al intentar modificar la tupla: {e}")

# 3. Diccionario
print(Fore.CYAN + "\nEjemplo de Diccionario:")
mi_diccionario = {"nombre": "Carlos", "edad": 30, "ciudad": "Santo Domingo"}
print(Fore.YELLOW + "Diccionario original:", mi_diccionario)

# Agregar una nueva clave-valor al diccionario
mi_diccionario["ocupacion"] = "programador"
print(Fore.GREEN + "Diccionario después de agregar una clave-valor:", mi_diccionario)

# Modificar un valor en el diccionario
mi_diccionario["edad"] = 31
print(Fore.GREEN + "Diccionario después de modificar un valor:", mi_diccionario)

# 4. Conjunto (Set)
print(Fore.CYAN + "\nEjemplo de Conjunto (Set):")
mi_conjunto = {1, 2, 3, 4, 5}
print(Fore.YELLOW + "Conjunto original:", mi_conjunto)

# Intentamos agregar un valor duplicado (un set no permite duplicados)
mi_conjunto.add(3)
print(Fore.GREEN + "Conjunto después de agregar un valor duplicado:", mi_conjunto)

# Eliminar un valor del conjunto
mi_conjunto.remove(4)
print(Fore.RED + "Conjunto después de eliminar un valor:", mi_conjunto)

# Verificar si un elemento existe en el conjunto
if 2 in mi_conjunto:
    print(Fore.MAGENTA + "El número 2 está en el conjunto.")
else:
    print(Fore.MAGENTA + "El número 2 no está en el conjunto.")
