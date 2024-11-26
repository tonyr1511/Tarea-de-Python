# Algoritmo para verificar si un número es perfecto

def es_numero_perfecto(numero):
    """Verifica si un número es perfecto"""
    if numero <= 0:
        return False  # Los números negativos y el 0 no son números perfectos
    
    suma_divisores = 0
    
    # Encontramos los divisores de 'numero'
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i  # Sumamos los divisores
    
    # Si la suma de los divisores es igual al número, es un número perfecto
    return suma_divisores == numero

def main():
    # Solicitar un número al usuario
    while True:
        try:
            numero = int(input("Ingresa un número entero para verificar si es perfecto: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    
    # Verificar si el número es perfecto
    if es_numero_perfecto(numero):
        print(f"\nEl número {numero} es un número perfecto.")
    else:
        print(f"\nEl número {numero} NO es un número perfecto.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
