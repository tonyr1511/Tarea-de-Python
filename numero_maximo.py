# Algoritmo para encontrar el número más grande en una lista

def encontrar_numero_maximo(lista):
    """Encuentra el número más grande en una lista de números"""
    # Suponemos que el primer número es el más grande
    maximo = lista[0]
    
    # Recorremos la lista para encontrar el número más grande
    for numero in lista:
        if numero > maximo:
            maximo = numero  # Actualizamos el máximo si encontramos uno mayor
    
    return maximo

def main():
    # Solicitamos al usuario que ingrese una lista de números
    while True:
        try:
            lista = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
            if len(lista) == 0:
                print("Por favor, ingresa al menos un número.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa solo números enteros separados por espacios.")
    
    # Llamamos a la función para encontrar el número máximo
    numero_maximo = encontrar_numero_maximo(lista)
    
    # Mostramos el resultado
    print(f"\nEl número más grande en la lista es: {numero_maximo}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
