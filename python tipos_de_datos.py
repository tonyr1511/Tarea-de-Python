# Programa para ilustrar el uso de diferentes tipos de datos

def main():
    # Pedir al usuario un número entero
    entero = int(input("Ingresa un número entero: "))
    
    # Pedir al usuario un número decimal (flotante)
    flotante = float(input("Ingresa un número decimal (flotante): "))
    
    # Pedir al usuario una cadena de texto
    cadena = input("Ingresa una palabra o frase: ")
    
    # Pedir al usuario una lista de números
    lista = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
    
    # Mostrar los datos ingresados
    print("\nDatos ingresados:")
    print(f"Número entero: {entero} (Tipo: {type(entero)})")
    print(f"Número decimal (flotante): {flotante} (Tipo: {type(flotante)})")
    print(f"Cadena de texto: {cadena} (Tipo: {type(cadena)})")
    print(f"Lista de números: {lista} (Tipo: {type(lista)})")

    # Realizar algunas operaciones con los datos
    suma = entero + flotante
    concatenacion = cadena + " - Gracias por usar el programa."
    
    print("\nOperaciones con los datos ingresados:")
    print(f"Suma del número entero y flotante: {suma}")
    print(f"Concatenación de la cadena con un mensaje adicional: {concatenacion}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
